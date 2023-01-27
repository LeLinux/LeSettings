import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3
desktop_fixed = gtk.Fixed()

backgroud_cbtn = gtk.ColorButton()
backgroud_cbtn.set_color(gdk.Color(6682, 7453, 11051))
backgroud_cbtn.set_sensitive(0)
backgroud_cbtn.set_property("width-request", inc.win_w / 1.5)
backgroud_cbtn.set_property("height-request", inc.win_h / 1.5)

polybar_cbtn = gtk.ColorButton()
polybar_cbtn.set_color(gdk.Color(6682, 60000, 11051))
polybar_cbtn.set_sensitive(0)
polybar_cbtn.set_property("width-request", inc.win_w / 1.5)
polybar_cbtn.set_property("height-request", inc.win_h / 12)


plank_cbt = gtk.ColorButton()
plank_cbt.set_color(gdk.Color(7000, 50000, 30000))
plank_cbt.set_sensitive(0)
plank_cbt.set_property("width-request", inc.win_w / 3)
plank_cbt.set_property("height-request", inc.win_h / 12)

top_l = gtk.Label("Top panel")
top_l.get_style_context().add_class("label")
top_l.set_xalign(0)
top_l.set_property("width-request", inc.main_const_def)

down_l = gtk.Label("Down panel")
down_l.get_style_context().add_class("label")
down_l.set_xalign(0)
down_l.set_property("width-request", inc.main_const_def)

wal_l = gtk.Label("Wallpapers")
wal_l.get_style_context().add_class("label")
wal_l.set_xalign(0)
wal_l.set_property("width-request", inc.main_const_def)

hight_l1 = gtk.Label("Height")
hight_l1.get_style_context().add_class("label")
hight_l1.set_xalign(0)
hight_l1.set_property("width-request", inc.main_const_def)

hight_l2 = gtk.Label("Height")
hight_l2.get_style_context().add_class("label")
hight_l2.set_xalign(0)
hight_l2.set_property("width-request", inc.main_const_def)

width_l1 = gtk.Label("Width")
width_l1.get_style_context().add_class("label")
width_l1.set_xalign(0)
width_l1.set_property("width-request", inc.main_const_def)

width_l2 = gtk.Label("Width")
width_l2.get_style_context().add_class("label")
width_l2.set_xalign(0)
width_l2.set_property("width-request", inc.main_const_def)

value = 50
adjustment1 = gtk.Adjustment(value, 0, 100, 1, 10, 0)
adjustment2 = gtk.Adjustment(value, 0, 100, 1, 10, 0)
adjustment3 = gtk.Adjustment(value, 0, 100, 1, 10, 0)
adjustment4 = gtk.Adjustment(value, 0, 100, 1, 10, 0)

hight_s1 = gtk.HScale(adjustment=adjustment1)
hight_s1.set_property("width-request", inc.main_const_def)
hight_s1.set_vexpand(True)
hight_s1.set_hexpand(True)
hight_s1.set_draw_value(0)

hight_s2 = gtk.HScale(adjustment=adjustment2)
hight_s2.set_property("width-request", inc.main_const_def - inc.main_const_def / 12)
hight_s2.set_vexpand(True)
hight_s2.set_hexpand(True)
hight_s2.set_draw_value(0)

width_s1 = gtk.HScale(adjustment=adjustment3)
width_s1.set_property("width-request", inc.main_const_def)
width_s1.set_vexpand(True)
width_s1.set_hexpand(True)
width_s1.set_draw_value(0)

width_s2 = gtk.HScale(adjustment=adjustment4)
width_s2.set_property("width-request", inc.main_const_def)
width_s2.set_vexpand(True)
width_s2.set_hexpand(True)
width_s2.set_draw_value(0)

browse_b = gtk.Button(label="Browse")
browse_b.set_property("width-request", inc.main_const_def / 3)
browse_b.set_margin_start(inc.main_const_def /  2)


apply_b = gtk.Button(label="Apply")
apply_b.set_property("width-request", inc.main_const_def)

desktop_fixed.add(backgroud_cbtn)
desktop_fixed.move(backgroud_cbtn, inc.win_w / 14, inc.win_h / 6)

desktop_fixed.add(polybar_cbtn)
desktop_fixed.move(polybar_cbtn, inc.win_w / 14, inc.win_h / 6)

desktop_fixed.add(plank_cbt)
desktop_fixed.move(plank_cbt, inc.win_w / 4.3, inc.win_h / 1.33)

desktop_fixed.add(top_l)
desktop_fixed.move(top_l, inc.win_w / 1.3, inc.win_h / 6)

desktop_fixed.add(hight_l1)
desktop_fixed.move(hight_l1, inc.win_w / 1.3, inc.win_h / 4)

desktop_fixed.add(hight_s1)
desktop_fixed.move(hight_s1, inc.win_w / 1.2, inc.win_h / 4.15)

desktop_fixed.add(width_l1)
desktop_fixed.move(width_l1, inc.win_w / 1.3, inc.win_h / 3)

desktop_fixed.add(width_s1)
desktop_fixed.move(width_s1, inc.win_w / 1.2, inc.win_h / 3.15)

desktop_fixed.add(down_l)
desktop_fixed.move(down_l, inc.win_w / 1.3, inc.win_h / 2.4)

desktop_fixed.add(hight_l2)
desktop_fixed.move(hight_l2, inc.win_w / 1.3, inc.win_h / 2)

desktop_fixed.add(hight_s2)
desktop_fixed.move(hight_s2, inc.win_w / 1.2, inc.win_h / 2.015)

desktop_fixed.add(width_l2)
desktop_fixed.move(width_l2, inc.win_w / 1.3, inc.win_h / 1.72)

desktop_fixed.add(width_s2)
desktop_fixed.move(width_s2, inc.win_w / 1.2, inc.win_h / 1.75)

desktop_fixed.add(wal_l)
desktop_fixed.move(wal_l, inc.win_w / 1.3, inc.win_h / 1.5)

desktop_fixed.add(browse_b)
desktop_fixed.move(browse_b, inc.win_w / 1.2, inc.win_h / 1.5)

desktop_fixed.add(apply_b)
desktop_fixed.move(apply_b, inc.win_w / 1.26, inc.win_h / 1.1)
