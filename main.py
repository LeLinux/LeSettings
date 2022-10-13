import gi
from screeninfo import get_monitors
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf

from lelib import *

sc_w, sc_h = get_monitors()[0].width, get_monitors()[0].height #get monitors resolution
win_w, win_h, w_const, h_const = sc_w, sc_h, 0.417, 0.31275 #set default constants

#that IF-ELSE block do dynamic change of window size by use screen resolution
if sc_w <= 1920 and sc_h <= 1080:
    win_w, win_h = 800, 600
else:
    win_w, win_h = sc_w * 0.417, sc_w * 0.31275




class Main(gtk.Window):
    def __init__(self):

        super().__init__(title="Settings")
        
        #CONSTANTS
        #=========
        #Main menu constants
        self.main_top_mar = (win_h - (win_w / 5) * 2) / 3 #margin-top constant
        self.main_const = win_w / 5#win_w / 5 #constant for button widht\height and margin-start
        self.icon_size = self.main_const * 0.85

        #ICONS
        #=====
        #PIXBUF-S
        #Main menu PIXBUF-s
        self.pixbuf_system_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/cs-windows.svg", width = self.icon_size, height = self.icon_size, preserve_aspect_ratio = 1)
        
        self.pixbuf_connections_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/preferences-system-network.svg", width = self.icon_size, height = self.icon_size, preserve_aspect_ratio = 1)
        
        self.pixbuf_devices_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/display-capplet.svg", width = self.icon_size, height = self.icon_size, preserve_aspect_ratio = 1)

        self.pixbuf_appearance_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/preferences-desktop-wallpaper.svg", width = self.icon_size, height = self.icon_size, preserve_aspect_ratio = 1)

        #PIXBUF-S to ICONS
        #=====
        #main menu icons
        self.system_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_system_b_icon)
        self.conn_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_connections_b_icon)
        self.devices_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_devices_b_icon)
        self.appearance_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_appearance_b_icon)
        #=====

        #main selector grid & components
        self.system_b = gtk.Button(label = "System")
        self.system_b.set_relief(gtk.ReliefStyle.NONE)
        self.system_b.set_image(self.system_b_icon)
        self.system_b.set_image_position(gtk.PositionType.TOP)
        self.system_b.set_use_underline(1)
        self.system_b.set_always_show_image(1)
        self.system_b.set_property("width-request", self.main_const)
        self.system_b.set_property("height-request", self.main_const)
        self.system_b.set_margin_top(self.main_top_mar)
        self.system_b.set_margin_start(self.main_const)
        self.system_b.connect("clicked", go2system)

        self.conns_b = gtk.Button(label = "Connections")
        self.conns_b.set_relief(gtk.ReliefStyle.NONE)
        self.conns_b.set_image(self.conn_b_icon)
        self.conns_b.set_image_position(gtk.PositionType.TOP)
        self.conns_b.set_use_underline(1)
        self.conns_b.set_always_show_image(1)
        self.conns_b.set_property("width-request", self.main_const)
        self.conns_b.set_property("height-request", self.main_const)
        self.conns_b.set_margin_top(self.main_top_mar)
        self.conns_b.set_margin_start(self.main_const)
        
        self.appearance_b = gtk.Button(label = "Appearence")
        self.appearance_b.set_relief(gtk.ReliefStyle.NONE)
        self.appearance_b.set_image(self.appearance_b_icon)
        self.appearance_b.set_image_position(gtk.PositionType.TOP)
        self.appearance_b.set_use_underline(1)
        self.appearance_b.set_always_show_image(1)
        self.appearance_b.set_property("width-request", self.main_const)
        self.appearance_b.set_property("height-request", self.main_const)
        self.appearance_b.set_margin_top(self.main_top_mar)
        self.appearance_b.set_margin_start(self.main_const)


        self.devices_b = gtk.Button(label = "Devices")
        self.devices_b.set_relief(gtk.ReliefStyle.NONE)
        self.devices_b.set_image(self.devices_b_icon)
        self.devices_b.set_image_position(gtk.PositionType.TOP)
        self.devices_b.set_use_underline(1)
        self.devices_b.set_always_show_image(1)
        self.devices_b.set_property("width-request", self.main_const)
        self.devices_b.set_property("height-request", self.main_const)
        self.devices_b.set_margin_top(self.main_top_mar)
        self.devices_b.set_margin_start(self.main_const)

        self.selector_grid = gtk.Grid()
        self.selector_grid.add(self.system_b)
        self.selector_grid.attach(self.system_b, 1, 0, 2, 1)
        self.selector_grid.attach_next_to(self.conns_b, self.system_b, gtk.PositionType.RIGHT, 1, 1)
        self.selector_grid.attach_next_to(self.devices_b, self.system_b, gtk.PositionType.BOTTOM, 1, 1)
        self.selector_grid.attach_next_to(self.appearance_b, self.devices_b, gtk.PositionType.RIGHT, 1, 2)
        #===========
        #System grid
        
        self.back2menu = gtk.Button(label = "Back to menu")
        self.back2menu.set_relief(gtk.ReliefStyle.NONE)
        self.back2menu.set_property("width-request", self.main_const / 2)
        self.back2menu.connect("clicked", go2menu)


        self.sys_grid = gtk.Grid()
        self.sys_grid.add(self.back2menu)
        self.sys_grid.attach(self.back2menu, 1, 0, 2, 1)
        #===========
      
        self.main_fixed = gtk.Fixed()
        self.main_fixed.add(self.selector_grid)
        self.main_fixed.move(self.selector_grid, 0, 0)
        self.main_fixed.add(self.sys_grid)
        self.main_fixed.move(self.sys_grid, -1 * win_w - 100, -1 * win_h - 100)


        self.add(self.main_fixed)
        

        self.show_all()



    """def go2system(self, btn):
        print("[LOG] GO2SYSTEM function started")
        self.main_fixed.move(self.selector_grid, -1 * win_w - 100, -1 * win_h - 100)
        self.main_fixed.move(self.sys_grid, 0, 0)
        print("[LOG] GO2SYSTEM function finished")
    """
win = Main()
win.set_default_size(win_w, win_h)
win.set_resizable(0)
win.connect("destroy", gtk.main_quit)
set_win_init(win)
#win.show_all()
gtk.main()
