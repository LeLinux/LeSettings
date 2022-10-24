import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(4)

multitask_b = gtk.Button(label = "Multitasking")
multitask_b.set_relief(gtk.ReliefStyle.NONE)
multitask_b.get_style_context().add_class("button")
multitask_b.set_image(inc.multitask_b_icon)
multitask_b.set_image_position(gtk.PositionType.TOP)
multitask_b.set_use_underline(1)
multitask_b.set_always_show_image(1)
multitask_b.set_property("width-request", main_const)
multitask_b.set_property("height-request", main_const)
multitask_b.set_margin_top(main_top_mar)
multitask_b.set_margin_start(main_const)

themes_b = gtk.Button(label = "Themes")
themes_b.set_relief(gtk.ReliefStyle.NONE)
themes_b.get_style_context().add_class("button")
themes_b.set_image(inc.themes_b_icon)
themes_b.set_image_position(gtk.PositionType.TOP)
themes_b.set_use_underline(1)
themes_b.set_always_show_image(1)
themes_b.set_property("width-request", main_const)
themes_b.set_property("height-request", main_const)
themes_b.set_margin_top(main_top_mar)
themes_b.set_margin_start(main_const)

fonts_b = gtk.Button(label = "Fonts")
fonts_b.set_relief(gtk.ReliefStyle.NONE)
fonts_b.get_style_context().add_class("button")
fonts_b.set_image(inc.fonts_b_icon)
fonts_b.set_image_position(gtk.PositionType.TOP)
fonts_b.set_use_underline(1)
fonts_b.set_always_show_image(1)
fonts_b.set_property("width-request", main_const)
fonts_b.set_property("height-request", main_const)
fonts_b.set_margin_top(main_top_mar)
fonts_b.set_margin_start(main_const)

desktop_b = gtk.Button(label = "Desktop")
desktop_b.set_relief(gtk.ReliefStyle.NONE)
desktop_b.get_style_context().add_class("button")
desktop_b.set_image(inc.desktop_b_icon)
desktop_b.set_image_position(gtk.PositionType.TOP)
desktop_b.set_use_underline(1)
desktop_b.set_always_show_image(1)
desktop_b.set_property("width-request", main_const)
desktop_b.set_property("height-request", main_const)
desktop_b.set_margin_top(main_top_mar)
desktop_b.set_margin_start(main_const)

appear_menu = gtk.Grid()
appear_menu.add(multitask_b)
appear_menu.attach(multitask_b, 1, 0, 2, 1)
appear_menu.attach_next_to(themes_b, multitask_b, gtk.PositionType.RIGHT, 1, 1)
appear_menu.attach_next_to(fonts_b, multitask_b, gtk.PositionType.BOTTOM, 1, 1)
appear_menu.attach_next_to(desktop_b, fonts_b, gtk.PositionType.RIGHT, 1, 2)
