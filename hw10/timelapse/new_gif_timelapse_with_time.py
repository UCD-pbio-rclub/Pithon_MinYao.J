from picamera import PiCamera
from os import system
from time import sleep
import time

camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(18):
    dir_path='/home/pi/Desktop/timelapse/'
    timestr=time.strftime("%Y%m%d-%H%M%S")
    file_name=timestr + '.jpg'
    path=dir_path+file_name        #abs path of file
    camera.capture(path) 
    sleep(600)

system('convert -delay 20 -loop 0 /home/pi/Desktop/timelapse/*.jpg /home/pi/Desktop/timelapse/animation.gif')
print('done')
