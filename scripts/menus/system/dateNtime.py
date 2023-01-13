import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

autotime_l = gtk.Label("Automatic set time")
autotime_l.get_style_context().add_class("label")
autotime_l.set_xalign(0)
autotime_l.set_property("width-request", inc.main_const_def)
autotime_l.set_margin_start(inc.win_w / 4)
autotime_l.set_margin_top(inc.win_h / 3.1)

time_l = gtk.Label("Time")
time_l.get_style_context().add_class("label")
time_l.set_property("width-request", inc.main_const_def)
time_l.set_xalign(0)
time_l.set_margin_start(mar_start)
time_l.set_margin_top(mar_top)


time_format = gtk.Label("Time format")
time_format.get_style_context().add_class("label")
time_format.set_property("width-request", inc.main_const_def)
time_format.set_xalign(0)
time_format.set_margin_start(mar_start)
time_format.set_margin_top(mar_top)



time_formats = ["24-hour", "AM/PM"]

time_format_selector = gtk.ComboBoxText()
for i in time_formats:
    time_format_selector.append_text(i)
time_format_selector.set_margin_start(mar_start / 2)
time_format_selector.set_margin_top(mar_top)

autotime_switcher = gtk.Switch()
autotime_switcher.set_margin_start(mar_start / 1.55)
autotime_switcher.set_margin_top(inc.win_h / 3.1)

autodate_l = gtk.Label("Automatic set date")
autodate_l.get_style_context().add_class("label")
autodate_l.set_xalign(0)
autodate_l.set_property("width-request", inc.main_const_def)
autodate_l.set_margin_start(inc.win_w / 4)
autodate_l.set_margin_top(mar_top)

date_l = gtk.Label("Date")
date_l.get_style_context().add_class("label")
date_l.set_property("width-request", inc.main_const_def)
date_l.set_xalign(0)
date_l.set_margin_start(mar_start)
date_l.set_margin_top(mar_top)

autodate_switcher = gtk.Switch()
autodate_switcher.set_margin_start(217)
autodate_switcher.set_margin_top(mar_top)

spacer_l = gtk.Label(" ")
spacer_l.get_style_context().add_class("label")
spacer_l.set_property("width-request", inc.main_const_def)
spacer_l.set_xalign(0)
spacer_l.set_margin_start(mar_start)
spacer_l.set_margin_top(mar_top)

dnt_grid = gtk.Grid()
dnt_grid.add(autotime_l)
dnt_grid.attach(autotime_l, 1, 1, 0, 0)
dnt_grid.attach_next_to(autotime_switcher, autotime_l, gtk.PositionType.RIGHT, 1, 1)
dnt_grid.attach_next_to(time_l, autotime_l, gtk.PositionType.BOTTOM, 1, 1)
dnt_grid.attach_next_to(time_format, time_l, gtk.PositionType.BOTTOM, 1, 1)
dnt_grid.attach_next_to(time_format_selector, time_format, gtk.PositionType.RIGHT, 1, 1)
dnt_grid.attach_next_to(spacer_l, time_format, gtk.PositionType.BOTTOM, 1, 1)
dnt_grid.attach_next_to(autodate_l, spacer_l, gtk.PositionType.BOTTOM, 1, 1)
dnt_grid.attach_next_to(autodate_switcher, autodate_l, gtk.PositionType.RIGHT, 1, 1)
dnt_grid.attach_next_to(date_l, autodate_l, gtk.PositionType.BOTTOM, 1, 1)
