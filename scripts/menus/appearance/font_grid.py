import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns
import scripts.lesetlib as lsl

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

font_l = gtk.Label("Font")
font_l.get_style_context().add_class("label")
font_l.set_xalign(0)
font_l.set_property("width-request", inc.main_const_def)
font_l.set_margin_start(mar_start)
font_l.set_margin_top(inc.win_h / 3.1)

test_f_l = gtk.Label("Test text")
test_f_l.get_style_context().add_class("label")
test_f_l.set_property("width-request", inc.main_const_def)
test_f_l.set_xalign(0)
test_f_l.set_margin_start(mar_start)
test_f_l.set_margin_top(mar_top)

fonts_formats = ["Times new Roman", "Arial"]
font_format_selector = gtk.ComboBoxText()
for i in fonts_formats:
    font_format_selector.append_text(i)
font_format_selector.set_margin_start(mar_start)
font_format_selector.set_margin_top(mar_top)

font_grid = gtk.Grid()
font_grid.add(font_l)
font_grid.attach(font_l, 1, 1, 0, 0)
font_grid.attach_next_to(font_format_selector, font_l, gtk.PositionType.RIGHT, 1, 1)
font_grid.attach_next_to(test_f_l, font_l, gtk.PositionType.BOTTOM, 1, 1)
