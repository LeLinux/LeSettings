import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

back2menu = gtk.Button(label = "Back")
back2menu.set_relief(gtk.ReliefStyle.NONE)

back2system = gtk.Button(label = "Back")
back2system.set_relief(gtk.ReliefStyle.NONE)

headb_fixed = gtk.Fixed()

headb_fixed.add(back2menu)
headb_fixed.move(back2menu, -1 * inc.main_const_def, -1 * inc.main_const_def)

headb_fixed.add(back2system)
headb_fixed.move(back2system, -1 * inc.main_const_def, -1 * inc.main_const_def)

gtk.StyleContext.add_class(headb_fixed.get_style_context(), "linked")


headb = gtk.HeaderBar(title = "LeSettings")
headb.set_show_close_button(1)
headb.add(headb_fixed)
