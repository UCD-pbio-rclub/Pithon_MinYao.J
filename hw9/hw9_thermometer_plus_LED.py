# 05_thermomether_plus.py

from tkinter import *           # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time, math


C = 0.33 # uF 
R1 = 1000 # Ohms
B = 3800.0 # The thermistor constant - change this for a different thermistor
R0 = 1000.0 # The resistance of the thermistor at 25C -change for different thermistor


# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in series
# pin b discharges the capacitor through a fixed 1k resistor 

a_pin = 18
b_pin = 23
led_pin = 24

GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(0)

# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

# return the time taken for the voltage on the capacitor to count as a digital input HIGH
# than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000 # microseconds

# Take an analog readin as the time taken to charge after first discharging the capacitor
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

# Convert the time taken to charge the cpacitor into a value of resistance
# To reduce errors, do it lots of times and take the average.
def read_resistance():
    n = 10
    total = 0;
    for i in range(0, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r


def read_temp_c():
    R = read_resistance()
    t0 = 273.15     # 0 deg C in K
    t25 = t0 + 25.0 # 25 deg C in K
    # Steinhart-Hart equation - Google it
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = (1/inv_T - t0)
    return T


# group together all of the GUI code into a class called App
class App:

    # this function gets called when the app is created
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Temp C', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    # Update the temperature reading
    def update_reading(self):
        temp_c = read_temp_c()
        if temp_c*10-180 > 100:
            duty = 100
        if temp_c*10-180 < 100:
            duty = temp_c*10-180
        pwm_led.ChangeDutyCycle(duty)
        time.sleep(0.5)
        reading_str = "{:.2f}".format(temp_c)
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading)

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('Thermometer')
app = App(root)
root.geometry("400x300+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
