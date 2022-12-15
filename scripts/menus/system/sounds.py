import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = 20, 20

volume_l = gtk.Label("System volume")
volume_l.get_style_context().add_class("label")
volume_l.set_xalign(0)
volume_l.set_property("width-request", inc.main_const_def)
volume_l.set_margin_start(mar_start)
volume_l.set_margin_top(inc.win_h / 20)

output_l = gtk.Label("Output")
output_l.get_style_context().add_class("label")
output_l.set_xalign(0)
output_l.set_property("width-request", inc.main_const_def)
output_l.set_margin_start(mar_start)
output_l.set_margin_top(inc.win_h / 20)

input_l = gtk.Label("Input")
input_l.get_style_context().add_class("label")
input_l.set_xalign(0)
input_l.set_property("width-request", inc.main_const_def)
input_l.set_margin_start(mar_start)
input_l.set_margin_top(inc.win_h / 20)

balance_l1 = gtk.Label("Balance")
balance_l1.get_style_context().add_class("label")
balance_l1.set_xalign(0)
balance_l1.set_property("width-request", inc.main_const_def)
balance_l1.set_margin_start(mar_start)
balance_l1.set_margin_top(inc.win_h / 20)

balance_l2 = gtk.Label("Balance")
balance_l2.get_style_context().add_class("label")
balance_l2.set_xalign(0)
balance_l2.set_property("width-request", inc.main_const_def)
balance_l2.set_margin_start(mar_start)
balance_l2.set_margin_top(inc.win_h / 20)

value = 50
adjustment = gtk.Adjustment(value, 0, 100, 1, 10, 0)

volume_scale = gtk.HScale(adjustment=adjustment)
volume_scale.set_value_pos(gtk.PositionType.BOTTOM)
volume_scale.set_vexpand(True)
volume_scale.set_hexpand(True)
volume_scale.set_draw_value(0)

balance_s1 = gtk.HScale(adjustment=adjustment)
balance_s1.set_value_pos(gtk.PositionType.BOTTOM)
balance_s1.set_vexpand(True)
balance_s1.set_hexpand(True)
balance_s1.set_draw_value(0)

balance_s2 = gtk.HScale(adjustment=adjustment)
balance_s2.set_value_pos(gtk.PositionType.BOTTOM)
balance_s2.set_vexpand(True)
balance_s2.set_hexpand(True)
balance_s2.set_draw_value(0)

dummy_b1 = gtk.Button(label="Dummy")
dummy_b1.set_property("width-request", inc.main_const_def)
dummy_b1.set_margin_start(mar_start)
dummy_b1.set_margin_top(inc.win_h / 20)

dummy_b2 = gtk.Button(label="Dummy")
dummy_b2.set_property("width-request", inc.main_const_def)
dummy_b2.set_margin_start(mar_start)
dummy_b2.set_margin_top(inc.win_h / 20)

test_b1 = gtk.Button(label="Test")
test_b1.set_property("width-request", inc.main_const_def)
test_b1.set_margin_start(mar_start)
test_b1.set_margin_top(inc.win_h / 20)

test_b2 = gtk.Button(label="Test")
test_b2.set_property("width-request", inc.main_const_def)
test_b2.set_margin_start(mar_start)
test_b2.set_margin_top(inc.win_h / 20)

sound_grid = gtk.Grid()
sound_grid.add(volume_l)
sound_grid.attach(volume_l, 1, 1, 0, 0)
sound_grid.attach_next_to(volume_scale, volume_l, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(output_l, volume_scale, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(dummy_b1, output_l, gtk.PositionType.RIGHT, 1, 1)
sound_grid.attach_next_to(test_b1, dummy_b1, gtk.PositionType.RIGHT, 1, 1)
sound_grid.attach_next_to(balance_l1, output_l, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(balance_s1, balance_l1, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(input_l, balance_s1, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(dummy_b2, input_l, gtk.PositionType.RIGHT, 1, 1)
sound_grid.attach_next_to(test_b2, dummy_b2, gtk.PositionType.RIGHT, 1, 1)
sound_grid.attach_next_to(balance_l2, input_l, gtk.PositionType.BOTTOM, 1, 1)
sound_grid.attach_next_to(balance_s2, balance_l2, gtk.PositionType.BOTTOM, 1, 1)
