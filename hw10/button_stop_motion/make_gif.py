from os import system

system('convert -delay 50 -loop 0 /home/pi/animation/frame*.jpg /home/pi/animation/animation.gif')
print('done')
