import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
import os
from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

sensativity_l = gtk.Label("Sensativity")
sensativity_l.get_style_context().add_class("label")
sensativity_l.set_xalign(0)
sensativity_l.set_property("width-request", inc.main_const_def)
sensativity_l.set_margin_start(mar_start)
sensativity_l.set_margin_top(inc.win_h / 5)

active_l = gtk.Label("Active button")
active_l.get_style_context().add_class("label")
active_l.set_xalign(0)
active_l.set_property("width-request", inc.main_const_def)
active_l.set_margin_start(mar_start)
active_l.set_margin_top(inc.win_h / 20)

value = 50
adjustment1 = gtk.Adjustment(value, 0, 100, 1, 10, 0)

sensativity_scale = gtk.HScale(adjustment=adjustment1)
sensativity_scale.set_value_pos(gtk.PositionType.BOTTOM)
sensativity_scale.set_vexpand(True)
sensativity_scale.set_hexpand(True)
sensativity_scale.set_draw_value(0)
sensativity_scale.set_margin_start(inc.win_w / 6)
sensativity_scale.set_margin_top(inc.win_h / 4)

active_formats = ["Left", "Right"]

active_selector = gtk.ComboBoxText()
for i in active_formats:
    active_selector.append_text(i)
active_selector.set_margin_start(mar_start / 2)
active_selector.set_margin_top(mar_top)

mouse_grid = gtk.Grid()
mouse_grid.add(sensativity_l)
mouse_grid.attach(sensativity_l, 1, 1, 0, 0)
mouse_grid.attach_next_to(sensativity_scale, sensativity_l, gtk.PositionType.RIGHT, 1, 1)
mouse_grid.attach_next_to(active_l, sensativity_l, gtk.PositionType.BOTTOM, 1, 1)
mouse_grid.attach_next_to(active_selector, active_l, gtk.PositionType.RIGHT, 1, 1)
