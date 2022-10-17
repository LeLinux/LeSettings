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
langNreg.set_image(inc.langNreg_b_icon)
langNreg.set_image_position(gtk.PositionType.TOP)
langNreg.set_use_underline(1)
langNreg.set_always_show_image(1)

dataNtime = gtk.Button(label = "Date & Time")
dataNtime.set_relief(gtk.ReliefStyle.NONE)
dataNtime.set_property("width-request", inc.main_const)
dataNtime.set_property("height-request", inc.main_const)
dataNtime.set_margin_top(inc.main_top_mar)


sys_grid = gtk.Grid()
sys_grid.add(langNreg)
sys_grid.attach(langNreg, 1, 2, 1, 1)