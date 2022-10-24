from screeninfo import get_monitors
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf

#that IF-ELSE block do dynamic change of window size by use screen resolution




class Datas:
    def __init__(self):
        self.win_w, self.win_h = get_monitors()[0].width, get_monitors()[0].height #get monitors resolution
        self.w_const, self.h_const = 0.417, 0.31275 #set default constants

        if self.win_w <= 1920 and self.win_h <= 1080:
            self.win_w, self.win_h = 800, 600
        else:
            self.win_w, self.win_h = self.win_w * 0.417, self.win_w * 0.31275
        self.main_top_mar_def = (self.win_h - (self.win_w / 5) * 2) #margin-top constant
        self.main_const_def = self.win_w / 5#win_w / 5 #constant for button widht\height and margin-start
        self.icon_size_def = self.main_const_def * 0.85
        #self.main_const = self.main_const_def
        #self.main_top_mar = self.main_top_mar_def
        print("[LOG] Window width " + str(self.win_w))
        print("[LOG] Window height " + str(self.win_h))
        #ICONS
        #=====
        #PIXBUF-S
        #Main menu PIXBUF-s
        self.pixbuf_system_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/cs-windows.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        self.pixbuf_connections_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/preferences-system-network.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        self.pixbuf_devices_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/display-capplet.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        self.pixbuf_appearance_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/preferences-desktop-wallpaper.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        #System menu PIXBUF-s
        self.pixbuf_langNreg_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/config-language.svg", width = self.icon_size_def* 0.77, height = self.icon_size_def * 0.77, preserve_aspect_ratio = 1)

        self.pixbuf_dateNtime_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/apps/scalable/clock.svg", width = self.icon_size_def * 0.77, height = self.icon_size_def * 0.77, preserve_aspect_ratio = 1)

        self.pixbuf_users_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/preferences-system-users.svg", width = self.icon_size_def* 0.77, height = self.icon_size_def* 0.77, preserve_aspect_ratio = 1)

        self.pixbuf_sysinfo_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/preferences-desktop-default-applications.svg", width = self.icon_size_def* 0.77, height = self.icon_size_def* 0.77, preserve_aspect_ratio = 1)

        self.pixbuf_sound_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/apps/scalable/gnome-mixer.svg", width = self.icon_size_def* 0.77, height = self.icon_size_def* 0.77, preserve_aspect_ratio = 1)

        self.pixbuf_power_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/apps/scalable/preferences-system-power.svg", width = self.icon_size_def* 0.77, height = self.icon_size_def* 0.77, preserve_aspect_ratio = 1)

        #connection menu PIXBUF-s
        self.pixbuf_wifi_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/apps/scalable/spotify.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_bluetooth_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/apps/scalable/bluetooth.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_ethernet_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="/usr/share/icons/candy-icons/preferences/scalable/preferences-system-network-ethernet.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        #devices menu PIXBUF-s
        self.pixbuf_displays_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/display-capplet.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_keyboard_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/devices/scalable/input-keyboard.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_mouse_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/devices/scalable/input-mouse.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_printers_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/cs-printer.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        #appearance menu PIXBUF-s
        self.pixbuf_multitask_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/cs-themes.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_themes_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/preferences/scalable/preferences-theme.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_fonts_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/apps/scalable/fonts.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)
        self.pixbuf_desktop_b_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename = "/usr/share/icons/candy-icons/apps/scalable/deepin-show-desktop.svg", width = self.icon_size_def, height = self.icon_size_def, preserve_aspect_ratio = 1)

        #PIXBUF-S to ICONS
        #=====
        #main menu icons
        self.system_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_system_b_icon)
        self.conn_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_connections_b_icon)
        self.devices_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_devices_b_icon)
        self.appearance_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_appearance_b_icon)

        #System menu icons
        self.langNreg_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_langNreg_b_icon)
        self.dateNtime_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_dateNtime_b_icon)
        self.users_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_users_b_icon)
        self.sysinfo_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_sysinfo_b_icon)
        self.sound_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_sound_b_icon)
        self.power_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_power_b_icon)

        #connections menu icons
        self.wifi_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_wifi_b_icon)
        self.bluetooth_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_bluetooth_b_icon)
        self.ethernet_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_ethernet_b_icon)

        #devices menu icons
        self.displays_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_displays_b_icon)
        self.keyboard_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_keyboard_b_icon)
        self.mouse_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_mouse_b_icon)
        self.printers_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_printers_b_icon)

        #appearance menu icons
        self.multitask_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_multitask_b_icon)
        self.themes_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_themes_b_icon)
        self.fonts_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_fonts_b_icon)
        self.desktop_b_icon = gtk.Image.new_from_pixbuf(self.pixbuf_desktop_b_icon)


inc = Datas()

def get_consts(button_nums):
    if button_nums == 3:
        return inc.main_const_def, inc.main_top_mar_def / 1.35
    elif button_nums == 4:
        return inc.main_const_def, inc.main_top_mar_def / 3
    elif 5 <= button_nums <= 6:
        return inc.main_const_def * 3/4 - 0.04 * inc.main_const_def, inc.main_top_mar_def / 2.5
    elif 7 <= button_nums <= 12:
        return inc.main_const_def * 3/4, inc.main_top_mar_def / 7
