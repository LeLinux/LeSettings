import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

autotime_l = gtk.Label("Automatic set time")
autotime_l.get_style_context().add_class("label")
autotime_l.set_xalign(0)
autotime_l.set_property("width-request", inc.main_const_def)
#autotime_l.set_property("height-request", inc.main_const_def)
autotime_l.set_margin_start(inc.win_w / 4)
autotime_l.set_margin_top(inc.win_h / 24)

time_l = gtk.Label("Time")
time_l.get_style_context().add_class("label")
time_l.set_property("width-request", inc.main_const_def)
time_l.set_xalign(0)
time_l.set_margin_start(inc.win_w / 4)
time_l.set_margin_top(inc.win_h / 24)


dnt_grid = gtk.Grid()
dnt_grid.add(autotime_l)
dnt_grid.attach(autotime_l, 1, 1, 0, 0)
dnt_grid.attach_next_to(time_l, autotime_l, gtk.PositionType.BOTTOM, 1, 1)
