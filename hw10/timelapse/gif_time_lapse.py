from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(10):
    camera.capture('/home/pi/Desktop/image{0:04d}.jpg'.format(i))
    sleep(1800)

system('convert -delay 50 -loop 0 /home/pi/Desktop/image*.jpg /home/pi/Desktop/animation.gif')
print('done')
