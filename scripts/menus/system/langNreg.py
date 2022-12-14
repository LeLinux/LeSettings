import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_start = inc.main_const_def / 10
mar_top = mar_start

lang_l = gtk.Label("Language")
lang_l.get_style_context().add_class("label")
lang_l.set_xalign(0)
lang_l.set_property("width-request", inc.main_const_def)
lang_l.set_margin_start(inc.win_w/3.2)
lang_l.set_margin_top(inc.win_h/3.2)

reg_l = gtk.Label("Region")
reg_l.get_style_context().add_class("label")
reg_l.set_xalign(0)
reg_l.set_property("width-request", inc.main_const_def)
reg_l.set_margin_start(inc.win_w/3.2)
reg_l.set_margin_top(inc.win_h*0.05)

lang_list = ["Russian", "Engish"]
langs_selector = gtk.ComboBoxText()
for i in lang_list:
    langs_selector.append_text(i)
langs_selector.set_margin_start(mar_start)
langs_selector.set_margin_top(inc.win_h/3.2)

reg_list = ["Europe/Moscow", "USA/New-York"]
reg_selector = gtk.ComboBoxText()
for i in reg_list:
    reg_selector.append_text(i)
reg_selector.set_margin_start(mar_start)
reg_selector.set_margin_top(mar_top)

lnr_grid = gtk.Grid()
lnr_grid.add(lang_l)
lnr_grid.attach(lang_l, 1, 1, 0, 0)
lnr_grid.attach_next_to(langs_selector, lang_l, gtk.PositionType.RIGHT, 1, 1)
lnr_grid.attach_next_to(reg_l, lang_l, gtk.PositionType.BOTTOM, 1, 1)
lnr_grid.attach_next_to(reg_selector, reg_l, gtk.PositionType.RIGHT, 1, 1)
