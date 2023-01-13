import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

languages_l = gtk.Label("Languages layout")
languages_l.get_style_context().add_class("label")
languages_l.set_xalign(0)
languages_l.set_property("width-request", inc.main_const_def)
languages_l.set_margin_start(inc.win_w/ 2.5)
languages_l.set_margin_top(inc.win_h / 4)

layoutslist = ["Русский", "Engish", "+"]
buttons = []

for i in range(len(layoutslist)):
    btn_tmp = gtk.Button(label = layoutslist[i])
    btn_tmp.set_property("width-request", inc.win_w/2)
    btn_tmp.set_property("height-request", inc.win_h/10)
    btn_tmp.set_relief(gtk.ReliefStyle.NONE)
    buttons.append(btn_tmp)

box = gtk.VBox()
for i in buttons:
    box.pack_start(i, 0, 0, 0)

layouts = gtk.ScrolledWindow()
layouts.set_property("width-request", inc.win_w/2)
layouts.set_property("height-request", inc.win_h*0.75)
layouts.set_margin_top(inc.win_h/20)
layouts.set_margin_start(inc.win_w/4.2)
layouts.add(box)

shortcuts_b = gtk.Button(label="Shortuts")
shortcuts_b.set_property("width-request", inc.main_const_def)
shortcuts_b.set_margin_start(mar_start)
shortcuts_b.set_margin_top(inc.win_h/10)

keyboard_grid = gtk.Grid()
keyboard_grid.add(languages_l)
keyboard_grid.attach(languages_l, 1, 1, 0, 0)
keyboard_grid.attach_next_to(layouts, languages_l, gtk.PositionType.BOTTOM, 1, 1)
keyboard_grid.attach_next_to(shortcuts_b, layouts, gtk.PositionType.BOTTOM, 1, 1)
