from screeninfo import get_monitors  
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf

sc_w, sc_h = get_monitors()[0].width, get_monitors()[0].height #get monitors resolution
win_w, win_h, w_const, h_const = sc_w, sc_h, 0.417, 0.31275 #set default constants

#that IF-ELSE block do dynamic change of window size by use screen resolution


class Datas:
    def __init__(self):
        if sc_w <= 1920 and sc_h <= 1080:
            win_w, win_h = 800, 600
        else:
            win_w, win_h = sc_w * 0.417, sc_w * 0.31275
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

inc = Datas()
