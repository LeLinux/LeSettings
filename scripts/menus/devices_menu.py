import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(4)

displays_b = gtk.Button(label = "Displays")
displays_b.set_relief(gtk.ReliefStyle.NONE)
displays_b.get_style_context().add_class("button")
displays_b.set_image(inc.displays_b_icon)
displays_b.set_image_position(gtk.PositionType.TOP)
displays_b.set_use_underline(1)
displays_b.set_always_show_image(1)
displays_b.set_property("width-request", main_const)
displays_b.set_property("height-request", main_const)
displays_b.set_margin_top(main_top_mar)
displays_b.set_margin_start(main_const)

keyboard_b = gtk.Button(label = "Keyboard")
keyboard_b.set_relief(gtk.ReliefStyle.NONE)
keyboard_b.get_style_context().add_class("button")
keyboard_b.set_image(inc.keyboard_b_icon)
keyboard_b.set_image_position(gtk.PositionType.TOP)
keyboard_b.set_use_underline(1)
keyboard_b.set_always_show_image(1)
keyboard_b.set_property("width-request", main_const)
keyboard_b.set_property("height-request", main_const)
keyboard_b.set_margin_top(main_top_mar)
keyboard_b.set_margin_start(main_const)

mouse_b = gtk.Button(label = "Mouse")
mouse_b.set_relief(gtk.ReliefStyle.NONE)
mouse_b.get_style_context().add_class("button")
mouse_b.set_image(inc.mouse_b_icon)
mouse_b.set_image_position(gtk.PositionType.TOP)
mouse_b.set_use_underline(1)
mouse_b.set_always_show_image(1)
mouse_b.set_property("width-request", main_const)
mouse_b.set_property("height-request", main_const)
mouse_b.set_margin_top(main_top_mar)
mouse_b.set_margin_start(main_const)

printers_b = gtk.Button(label = "Printers")
printers_b.set_relief(gtk.ReliefStyle.NONE)
printers_b.get_style_context().add_class("button")
printers_b.set_image(inc.printers_b_icon)
printers_b.set_image_position(gtk.PositionType.TOP)
printers_b.set_use_underline(1)
printers_b.set_always_show_image(1)
printers_b.set_property("width-request", main_const)
printers_b.set_property("height-request", main_const)
printers_b.set_margin_top(main_top_mar)
printers_b.set_margin_start(main_const)

devices_menu = gtk.Grid()
devices_menu.add(displays_b)
devices_menu.attach(displays_b, 1, 0, 2, 1)
devices_menu.attach_next_to(keyboard_b, displays_b, gtk.PositionType.RIGHT, 1, 1)
devices_menu.attach_next_to(mouse_b, displays_b, gtk.PositionType.BOTTOM, 1, 1)
devices_menu.attach_next_to(printers_b, mouse_b, gtk.PositionType.RIGHT, 1, 2)
