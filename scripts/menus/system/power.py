import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

display_l = gtk.Label("Display light")
display_l.get_style_context().add_class("label")
display_l.set_xalign(0)
display_l.set_property("width-request", inc.main_const_def)
display_l.set_margin_start(mar_start)
display_l.set_margin_top(inc.win_h / 20)

energy_l = gtk.Label("Energy saver")
energy_l.get_style_context().add_class("label")
energy_l.set_xalign(0)
energy_l.set_property("width-request", inc.main_const_def)
energy_l.set_margin_start(mar_start)
energy_l.set_margin_top(inc.win_h / 20)

battery_l = gtk.Label("Battery info")
battery_l.get_style_context().add_class("label")
battery_l.set_xalign(0)
battery_l.set_property("width-request", inc.main_const_def)
battery_l.set_margin_start(mar_start)
battery_l.set_margin_top(inc.win_h / 20)

value = 50
adjustment = gtk.Adjustment(value, 0, 100, 1, 10, 0)

display_scale = gtk.HScale(adjustment=adjustment)
display_scale.set_value_pos(gtk.PositionType.BOTTOM)
display_scale.set_vexpand(True)
display_scale.set_hexpand(True)
display_scale.set_draw_value(0)

energy_switcher = gtk.Switch()
energy_switcher.set_margin_start(mar_start)
energy_switcher.set_margin_top(inc.win_h / 3.1)

power_grid = gtk.Grid()
power_grid.add(display_l)
power_grid.attach(display_l, 1, 1, 0, 0)
power_grid.attach_next_to(display_scale, display_l, gtk.PositionType.BOTTOM, 1, 1)
power_grid.attach_next_to(energy_l, display_scale, gtk.PositionType.BOTTOM, 1, 1)
power_grid.attach_next_to(energy_switcher, energy_l, gtk.PositionType.RIGHT, 1, 1)
power_grid.attach_next_to(energy_l, battery_l, gtk.PositionType.BOTTOM, 1, 1)
