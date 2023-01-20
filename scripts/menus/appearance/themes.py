import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

themes_l = gtk.Label("Themes")
themes_l.get_style_context().add_class("label")
themes_l.set_xalign(0)
themes_l.set_property("width-request", inc.main_const_def)
themes_l.set_margin_start(inc.win_w/ 2.24)
themes_l.set_margin_top(inc.win_h / 8)

import os
themeslist = os.listdir("/usr/share/themes/")
buttons = []

for i in range(len(themeslist)):
    btn_tmp = gtk.Button(label = themeslist[i])
    btn_tmp.set_property("width-request", inc.win_w/2)
    btn_tmp.set_property("height-request", inc.win_h/15)
    btn_tmp.set_relief(gtk.ReliefStyle.NONE)
    buttons.append(btn_tmp)

box = gtk.VBox()
print(buttons)
for i in buttons:
    box.pack_start(i, 0, 0, 0)

themes = gtk.ScrolledWindow()
themes.set_property("width-request", inc.win_w/1.5)
themes.set_property("height-request", inc.win_h/2)
themes.set_margin_top(inc.win_h/20)
themes.set_margin_start(inc.win_w/6)
themes.add(box)

install_b = gtk.Button(label="Install new")
install_b.set_property("width-request", inc.main_const_def)
install_b.set_property("height-request", inc.win_h/15)
install_b.set_margin_start(inc.win_w/ 7)
install_b.set_margin_top(inc.win_h/20)

themes_grid = gtk.Grid()
themes_grid.add(themes_l)
themes_grid.attach(themes_l, 1, 1, 0, 0)
themes_grid.attach_next_to(themes, themes_l, gtk.PositionType.BOTTOM, 1, 1)
themes_grid.attach_next_to(install_b, themes, gtk.PositionType.BOTTOM, 1, 1)
