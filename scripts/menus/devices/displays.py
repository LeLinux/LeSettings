import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3
displays_fixed = gtk.Fixed()

backgroud_cbtn = gtk.ColorButton()
backgroud_cbtn.set_color(gdk.Color(6682, 7453, 11051))
backgroud_cbtn.set_sensitive(0)
backgroud_cbtn.set_property("width-request", inc.win_w / 1.6)
backgroud_cbtn.set_property("height-request", inc.win_h / 1.6)

resolut_l = gtk.Label("Resolution")
resolut_l.get_style_context().add_class("label")
resolut_l.set_xalign(0)
resolut_l.set_property("width-request", inc.main_const_def)

rotate_l = gtk.Label("Rotate")
rotate_l.get_style_context().add_class("label")
rotate_l.set_xalign(0)
rotate_l.set_property("width-request", inc.main_const_def)

display_formats = ["Display 1", "Display 2"]

display_selector = gtk.ComboBoxText()
for i in display_formats:
    display_selector.append_text(i)
display_selector.set_active(0)
display_selector.set_property("width-request", inc.main_const_def*1.3)

resolut_formats = ["1920x1080", "1280x720"]

resolut_selector = gtk.ComboBoxText()
for i in resolut_formats:
    resolut_selector.append_text(i)
resolut_selector.set_active(0)

rotate_formats = ["Left", "Right"]

rotate_selector = gtk.ComboBoxText()
for i in rotate_formats:
    rotate_selector.append_text(i)
rotate_selector.set_active(0)

apply_b = gtk.Button(label="apply")
apply_b.set_property("width-request", inc.main_const_def)

displays_fixed.add(backgroud_cbtn)
displays_fixed.move(backgroud_cbtn, inc.win_w / 14, inc.win_h / 5)

displays_fixed.add(display_selector)
displays_fixed.move(display_selector, inc.win_w / 1.4, inc.win_h / 5)

displays_fixed.add(resolut_l)
displays_fixed.move(resolut_l, inc.win_w / 1.4, inc.win_h / 3)

displays_fixed.add(resolut_selector)
displays_fixed.move(resolut_selector, inc.win_w / 1.18, inc.win_h / 3)

displays_fixed.add(rotate_l)
displays_fixed.move(rotate_l, inc.win_w / 1.4, inc.win_h / 2.3)

displays_fixed.add(rotate_selector)
displays_fixed.move(rotate_selector, inc.win_w / 1.18, inc.win_h / 2.3)

displays_fixed.add(apply_b)
displays_fixed.move(apply_b, inc.win_w / 1.3, inc.win_h / 1.2)