import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

langNreg = gtk.Button(label = "Language & Region")
langNreg.set_relief(gtk.ReliefStyle.NONE)
langNreg.set_property("width-request", inc.main_const)
langNreg.set_property("height-request", inc.main_const)
langNreg.set_margin_top(inc.main_top_mar)
langNreg.set_margin_start(inc.main_const)


sys_grid = gtk.Grid()
sys_grid.add(langNreg)
sys_grid.attach(langNreg, 1, 2, 1, 1)