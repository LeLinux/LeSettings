import gi
from screeninfo import get_monitors
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf

import scripts.iconsNconst as inc
import scripts.go2 as g2
import scripts.menus.main_menu as mm
import scripts.menus.system_grid as sg
import scripts.menus.headbar as hdb
import scripts.button_connect as btnc

sc_w, sc_h = get_monitors()[0].width, get_monitors()[0].height #get monitors resolution
win_w, win_h, w_const, h_const = sc_w, sc_h, 0.417, 0.31275 #set default constants

#that IF-ELSE block do dynamic change of window size by use screen resolution
if sc_w <= 1920 and sc_h <= 1080:
    win_w, win_h = 800, 600
else:
    win_w, win_h = sc_w * 0.417, sc_w * 0.31275




class Main(gtk.Window):
    def __init__(self):

        super().__init__()
        self.main_fixed = gtk.Fixed()
        self.main_fixed.add(mm.main_menu)
        self.main_fixed.move(mm.main_menu, 0, 0)
        self.main_fixed.add(sg.sys_grid)
        self.main_fixed.move(sg.sys_grid, -1 * win_w - 100, -1 * win_h - 100)


        self.add(self.main_fixed)
        self.set_titlebar(hdb.headb)
        btnc.btn_connect()
        self.show_all()

win = Main()
win.set_default_size(win_w, win_h)
win.set_resizable(0)
win.connect("destroy", gtk.main_quit)
g2.set_win_init(win)
#win.show_all()
gtk.main()