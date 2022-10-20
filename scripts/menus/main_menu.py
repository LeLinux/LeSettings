import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(4)

#main selector grid & components
system_b = gtk.Button(label = "System")
system_b.set_relief(gtk.ReliefStyle.NONE)
system_b.set_image(inc.system_b_icon)
system_b.set_image_position(gtk.PositionType.TOP)
system_b.set_use_underline(1)
system_b.set_always_show_image(1)
system_b.set_property("width-request", main_const)
system_b.set_property("height-request", main_const)
system_b.set_margin_top(main_top_mar)
system_b.set_margin_start(main_const)

conns_b = gtk.Button(label = "Connections")
conns_b.set_relief(gtk.ReliefStyle.NONE)
conns_b.set_image(inc.conn_b_icon)
conns_b.set_image_position(gtk.PositionType.TOP)
conns_b.set_use_underline(1)
conns_b.set_always_show_image(1)
conns_b.set_property("width-request", main_const)
conns_b.set_property("height-request", main_const)
conns_b.set_margin_top(main_top_mar)
conns_b.set_margin_start(main_const)

appearance_b = gtk.Button(label = "Appearence")
appearance_b.set_relief(gtk.ReliefStyle.NONE)
appearance_b.set_image(inc.appearance_b_icon)
appearance_b.set_image_position(gtk.PositionType.TOP)
appearance_b.set_use_underline(1)
appearance_b.set_always_show_image(1)
appearance_b.set_property("width-request", main_const)
appearance_b.set_property("height-request", main_const)
appearance_b.set_margin_top(main_top_mar)
appearance_b.set_margin_start(main_const)

devices_b = gtk.Button(label = "Devices")
devices_b.set_relief(gtk.ReliefStyle.NONE)
devices_b.set_image(inc.devices_b_icon)
devices_b.set_image_position(gtk.PositionType.TOP)
devices_b.set_use_underline(1)
devices_b.set_always_show_image(1)
devices_b.set_property("width-request", main_const)
devices_b.set_property("height-request", main_const)
devices_b.set_margin_top(main_top_mar)
devices_b.set_margin_start(main_const)

main_menu = gtk.Grid()
main_menu.add(system_b)
main_menu.attach(system_b, 1, 0, 2, 1)
main_menu.attach_next_to(conns_b, system_b, gtk.PositionType.RIGHT, 1, 1)
main_menu.attach_next_to(devices_b, system_b, gtk.PositionType.BOTTOM, 1, 1)
main_menu.attach_next_to(appearance_b, devices_b, gtk.PositionType.RIGHT, 1, 2)