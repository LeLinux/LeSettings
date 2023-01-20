import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

mar_top, mar_start = inc.win_h / 24, inc.win_h / 3

userlist = ["Root", "Nickname"]
buttons = []

for i in range(len(userlist)):
    btn_tmp = gtk.Button(label = userlist[i])
    btn_tmp.set_property("width-request", inc.win_w/2)
    btn_tmp.set_property("height-request", inc.win_h/10)
    btn_tmp.set_relief(gtk.ReliefStyle.NONE)
    btn_tmp.set_image(gtk.Image.new_from_pixbuf(inc.pixbuf_default_user_icon))
    btn_tmp.set_alignment(0, 0)
    btn_tmp.set_image_position(gtk.PositionType.LEFT)
    btn_tmp.set_use_underline(1)
    btn_tmp.set_always_show_image(1)
    buttons.append(btn_tmp)

btn_tmp = gtk.Button(label = "+")
btn_tmp.set_property("width-request", inc.win_w/2)
btn_tmp.set_property("height-request", inc.win_h/10)
btn_tmp.set_relief(gtk.ReliefStyle.NONE)
buttons.append(btn_tmp)

box = gtk.VBox()
print(buttons)
for i in buttons:
    box.pack_start(i, 0, 0, 0)

user = gtk.ScrolledWindow()
user.set_property("width-request", inc.win_w/2)
user.set_property("height-request", inc.win_h/1.5)
user.set_margin_top(inc.win_h/20)
user.set_margin_start(inc.win_w/4.2)
user.add(box)

user_grid = gtk.Grid()
user_grid.add(user)
user_grid.attach(user, 1, 1, 0, 0)
