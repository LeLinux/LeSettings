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
languages_l.set_margin_start(inc.win_w / 6)
languages_l.set_margin_top(inc.win_h / 4)

rus_b = gtk.Button(label="Русский")
rus_b.set_property("width-request", inc.main_const_def)
rus_b.set_margin_start(mar_start)
rus_b.set_margin_top(inc.win_h / 20)

en_b = gtk.Button(label="English")
en_b.set_property("width-request", inc.main_const_def)
en_b.set_margin_start(mar_start)
en_b.set_margin_top(inc.win_h / 20)

plus_b = gtk.Button(label="+")
plus_b.set_property("width-request", inc.main_const_def)
plus_b.set_margin_start(mar_start)
plus_b.set_margin_top(inc.win_h / 20)

shortcuts_b = gtk.Button(label="Shortuts")
shortcuts_b.set_property("width-request", inc.main_const_def)
shortcuts_b.set_margin_start(mar_start)
shortcuts_b.set_margin_top(inc.win_h / 20)

keyboard_grid = gtk.Grid()
keyboard_grid.add(languages_l)
keyboard_grid.attach(languages_l, 1, 1, 0, 0)
keyboard_grid.attach_next_to(rus_b, languages_l, gtk.PositionType.BOTTOM, 1, 1)
keyboard_grid.attach_next_to(en_b, rus_b, gtk.PositionType.BOTTOM, 1, 1)
keyboard_grid.attach_next_to(plus_b, en_b, gtk.PositionType.BOTTOM, 1, 1)
keyboard_grid.attach_next_to(shortcuts_b, en_b, gtk.PositionType.BOTTOM, 1, 1)
