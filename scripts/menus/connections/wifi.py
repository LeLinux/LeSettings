import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns
import scripts.lesetlib as lsl

lsl.get_wifi_list_ssid()
ssid_l = lsl.wifi_l_ssids

buttons = []
c_ssid = ""

for i in range(len(ssid_l)-2):
    btn_tmp = gtk.Button(label = ssid_l[i])
    btn_tmp.set_property("width-request", inc.win_w/2)
    btn_tmp.set_property("height-request", inc.win_h/12)
    c_ssid = ssid_l[i]
    btn_tmp.connect("clicked", lsl.connection_window )
    btn_tmp.set_relief(gtk.ReliefStyle.NONE)
    buttons.append(btn_tmp)

box = gtk.VBox()
for i in buttons:
    box.pack_start(i, 0, 0, 0)

wifi = gtk.ScrolledWindow()
wifi.set_property("width-request", inc.win_w/2)
wifi.set_property("height-request", inc.win_h*0.75)
wifi.set_margin_top(inc.win_h*0.75*0.15)
wifi.set_margin_start(inc.win_w*0.25)
wifi.add(box)
