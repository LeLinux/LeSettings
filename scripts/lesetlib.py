import subprocess as sb
import alsaaudio


#input
#-----
# mod: 0 - add num to Current volume level; 1 - set absolute volume lvl
# num: volume level num
def change_volume_level(mod, num):
    mixer = alsaaudio.Mixer()
    if(mod == 0):
        current = mixer.getvolume()
        mixer.setvolume(current[0] + num)
    else:
        mixer.setvolume(num)

#input
#-----
# display: display identificator
# width: new display width
# height: new display height
# rotate: left, right, normal, inverted #for more info check xrandr docs
# position: [x, y, x+, y+]
def change_display(display, widht, height, rotate, position):
    pass
