import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(6)


langNreg = gtk.Button(label = "Language & Region")
langNreg.set_relief(gtk.ReliefStyle.NONE)
langNreg.get_style_context().add_class("button")
langNreg.set_property("width-request", main_const)
langNreg.set_property("height-request", main_const)
langNreg.set_margin_top(main_top_mar)
langNreg.set_margin_start(main_const)
langNreg.set_image(inc.langNreg_b_icon)
langNreg.set_image_position(gtk.PositionType.TOP)
langNreg.set_use_underline(1)
langNreg.set_always_show_image(1)

dateNtime = gtk.Button(label = "  Date & Time")
dateNtime.get_style_context().add_class("button")
dateNtime.set_relief(gtk.ReliefStyle.NONE)
dateNtime.set_property("width-request", main_const)
dateNtime.set_property("height-request", main_const)
dateNtime.set_margin_top(main_top_mar)
dateNtime.set_margin_start(main_const)
dateNtime.set_image(inc.dateNtime_b_icon)
dateNtime.set_image_position(gtk.PositionType.TOP)
dateNtime.set_use_underline(1)
dateNtime.set_always_show_image(1)

users_b = gtk.Button(label = "Users")
users_b.set_relief(gtk.ReliefStyle.NONE)
users_b.get_style_context().add_class("button")
users_b.set_property("width-request", main_const)
users_b.set_property("height-request", main_const)
users_b.set_margin_top(main_top_mar)
users_b.set_margin_start(main_const)
users_b.set_image(inc.users_b_icon)
users_b.set_image_position(gtk.PositionType.TOP)
users_b.set_use_underline(1)
users_b.set_always_show_image(1)

sysinfo = gtk.Button(label = "System Info")
sysinfo.set_relief(gtk.ReliefStyle.NONE)
sysinfo.get_style_context().add_class("button")
sysinfo.set_property("width-request", main_const)
sysinfo.set_property("height-request", main_const)
sysinfo.set_margin_top(main_top_mar)
sysinfo.set_margin_start(main_const)
sysinfo.set_image(inc.sysinfo_b_icon)
sysinfo.set_image_position(gtk.PositionType.TOP)
sysinfo.set_use_underline(1)
sysinfo.set_always_show_image(1)

sound_b = gtk.Button(label = "Sound")
sound_b.set_relief(gtk.ReliefStyle.NONE)
sound_b.get_style_context().add_class("button")
sound_b.set_property("width-request", main_const)
sound_b.set_property("height-request", main_const)
sound_b.set_margin_top(main_top_mar)
sound_b.set_margin_start(main_const)
sound_b.set_image(inc.sound_b_icon)
sound_b.set_image_position(gtk.PositionType.TOP)
sound_b.set_use_underline(1)
sound_b.set_always_show_image(1)

power_b = gtk.Button(label = "Power")
power_b.set_relief(gtk.ReliefStyle.NONE)
power_b.get_style_context().add_class("button")
power_b.set_property("width-request", main_const)
power_b.set_property("height-request", main_const)
power_b.set_margin_top(main_top_mar)
power_b.set_margin_start(main_const)
power_b.set_image(inc.power_b_icon)
power_b.set_image_position(gtk.PositionType.TOP)
power_b.set_use_underline(1)
power_b.set_always_show_image(1)



sys_grid = gtk.Grid()
sys_grid.add(langNreg)
sys_grid.attach(langNreg, 1, 0, 2, 1)
sys_grid.attach_next_to(dateNtime, langNreg, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(sound_b, dateNtime, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(power_b, langNreg, gtk.PositionType.BOTTOM, 1, 1)
sys_grid.attach_next_to(users_b, power_b, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(sysinfo, users_b, gtk.PositionType.RIGHT, 1, 1)
