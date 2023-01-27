import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

root_btn = gtk.Button(label = "Root")
#root_btn.set_relief(gtk.Button(root_btn), GTK.RELIEF_NORMAL)
#root_btn.set_image(gtk_BUTTON(root_btn), image)
#root_btn.set_image_position(gtk_BUTTON(root_btn), GTK_POS_LEFT)
root_btn.set_property("width-request", inc.main_const_def)
#root_btn.set_xalign(0)
root_btn.set_margin_start(mar_start)
root_btn.set_margin_top(mar_top)


nick_btn = gtk.Button(label = "Nickname")
#nick_btn.set_relief(gtk.Button(nick_btn), GTK_RELIEF_NORMAL)
#nick_btn.set_image(gtk_BUTTON(nick_btn), image)
#nick_btn.set_image_position(gtk_BUTTON(nick_btn), GTK_POS_LEFT)
nick_btn.set_property("width-request", inc.main_const_def)
#nick_btn.set_align(0)
nick_btn.set_margin_start(mar_start)
nick_btn.set_margin_top(mar_top)


plus_btn = gtk.Button(label = "+")
plus_btn.set_property("width-request", inc.main_const_def)
#plus_btn.set_xalign(0)
plus_btn.set_margin_start(mar_start)
plus_btn.set_margin_top(mar_top)

user_grid = gtk.Grid()
user_grid.add(root_btn)
user_grid.attach(root_btn, 1, 1, 0, 0)
user_grid.attach_next_to(nick_btn, root_btn, gtk.PositionType.BOTTOM, 1, 1)
user_grid.attach_next_to(plus_btn, root_btn, gtk.PositionType.BOTTOM, 1, 1)
