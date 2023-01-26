import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk

from scripts.iconsNconst import *
import scripts.go2 as g2


desktop_fixed = gtk.Fixed()

backgroud_cbtn = gtk.ColorButton()
backgroud_cbtn.set_color(gdk.Color(6682, 7453, 11051))
backgroud_cbtn.set_sensitive(0)
backgroud_cbtn.set_property("width-request", inc.win_w / 2)
backgroud_cbtn.set_property("height-request", inc.win_h / 2)

polybar_cbtn = gtk.ColorButton()
polybar_cbtn.set_color(gdk.Color(6682, 60000, 11051))
polybar_cbtn.set_sensitive(0)
polybar_cbtn.set_property("width-request", inc.win_w / 2)
polybar_cbtn.set_property("height-request", inc.win_h / 16)


plank_cbt = gtk.ColorButton()
plank_cbt.set_color(gdk.Color(7000, 50000, 30000))
plank_cbt.set_sensitive(0)
plank_cbt.set_property("width-request", inc.win_w / 4)
plank_cbt.set_property("height-request", inc.win_h / 16)


desktop_fixed.add(backgroud_cbtn)
desktop_fixed.move(backgroud_cbtn, inc.win_w / 8, inc.win_h / 8)

desktop_fixed.add(polybar_cbtn)
desktop_fixed.move(polybar_cbtn, inc.win_w / 8, inc.win_h / 8)

desktop_fixed.add(plank_cbt)
desktop_fixed.move(plank_cbt, inc.win_w / 4, inc.win_h / 1.8)