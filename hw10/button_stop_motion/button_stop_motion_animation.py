from picamera import PiCamera
from time import sleep
from gpiozero import Button
from os import system
import time

button = Button(17)
camera = PiCamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break

system('convert -delay 50 -loop 0 /home/pi/animation/frame*.jpg /home/pi/animation/animation.gif')
print('done')
