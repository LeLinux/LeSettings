import subprocess as sb
import alsaaudio
from scripts.iconsNconst import *
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

import distro
import os
import cpuinfo

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

def get_wifi_list_ssid():
    ssid_l = sb.check_output(["timeout", "5s", "nmcli", "-f", "SSID", "dev", "wifi"]).decode("utf-8").split("\n")[1:]
    return ssid_l

wifi_ssid = "WIFI SSID. TODO"

class ConnectionWindow(gtk.Window):
    def __init__(self):
        global wifi_ssid
        super().__init__()
        self.set_default_size(inc.win_w/3 - inc.win_h/25, inc.win_h/6)
        self.set_resizable(0)
        self.connect("destroy", self.destroy)

        self.wifi_l = gtk.Label(wifi_ssid)
        self.wifi_l.get_style_context().add_class("label")
        self.wifi_l.set_property("width-request", inc.win_w/3 - inc.win_w/10)
        self.wifi_l.set_property("height-request", inc.win_h/40)
        self.wifi_l.set_margin_top(inc.win_w/30)
        self.wifi_l.set_margin_start(inc.win_w/30)


        self.pwd_entry = gtk.Entry()
        #self.pwd_entry.set_buffer("Password")
        self.pwd_entry.set_visibility(0)
        self.pwd_entry.set_property("width-request", inc.win_w/3 - inc.win_w/10)
        self.pwd_entry.set_property("height-request", inc.win_h/30)
        self.pwd_entry.set_margin_top(inc.win_h/50)
        self.pwd_entry.set_margin_start(inc.win_w/30)

        self.btn_cnnt = gtk.Button("Connect")
        self.btn_cnnt.get_style_context().add_class("button")
        self.btn_cnnt.set_property("width-request", inc.win_w/3 - inc.win_w/10)
        self.btn_cnnt.set_property("height-request", inc.win_h/30)
        self.btn_cnnt.set_margin_top(inc.win_h/50)
        self.btn_cnnt.set_margin_bottom(inc.win_w/30)
        self.btn_cnnt.set_margin_start(inc.win_w/30)

        self.auth_grid = gtk.Grid()
        self.auth_grid.add(self.wifi_l)
        self.auth_grid.attach(self.wifi_l, 1, 1, 1, 1)
        self.auth_grid.attach_next_to(self.pwd_entry, self.wifi_l, gtk.PositionType.BOTTOM, 1, 1)
        self.auth_grid.attach_next_to(self.btn_cnnt, self.pwd_entry, gtk.PositionType.BOTTOM, 1, 1)

        self.add(self.auth_grid)
        self.show_all()

def connection_window(btn):#, ssid):
    win_wifi = ConnectionWindow()


#output:
# [
# : distro name
# : RAM
# : CPU
# : GPU
# ]
# COMMENT: PLS, dont ask how it works. IDK
#TODO on my laptop, with integrated GPU, dont work GPU finding. Fix it
def get_sysinfo():
    __datas__ = []
    __datas__.append(distro.linux_distribution()[0]) #distro name
    __datas__.append(str((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))/(1024.**3))[:5]) #RAM size
    cpu = sb.check_output(["cat", "/proc/cpuinfo"]).decode("UTF-8").split("\n")
    for i in cpu:
        if "model name" in i:
            __datas__.append(i.split(":")[1])
            break
    gpu = sb.check_output(["clinfo"]).decode("UTF-8").split("\n")
    for i in gpu:
        if "Device Name" in i:
            spi = i.split(" ")
            nos = 0
            addable = ""
            for j in spi:
                if j == "":
                    nos += 1
                elif nos > 2:
                    addable += j + " "
            __datas__.append(addable)
            break
    return __datas__
