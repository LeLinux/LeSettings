import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import Gdk
import scripts.button_settings as btns

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(6)

langNreg = gtk.Button(label = "Language & Region")
btns.set_button_data(langNreg,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.langNreg_b_icon)

dateNtime = gtk.Button(label = "  Date & Time")
btns.set_button_data(dateNtime,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.dateNtime_b_icon)

users_b = gtk.Button(label = "Users")
btns.set_button_data(users_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.users_b_icon)

sysinfo = gtk.Button(label = "System Info")
btns.set_button_data(sysinfo,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.sysinfo_b_icon)

sound_b = gtk.Button(label = "Sound")
btns.set_button_data(sound_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.sound_b_icon)

power_b = gtk.Button(label = "Power")
btns.set_button_data(power_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.power_b_icon)

sys_grid = gtk.Grid()
sys_grid.add(langNreg)
sys_grid.attach(langNreg, 0, 0, 0, 0)
sys_grid.attach_next_to(dateNtime, langNreg, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(sound_b, dateNtime, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(power_b, langNreg, gtk.PositionType.BOTTOM, 1, 1)
sys_grid.attach_next_to(users_b, power_b, gtk.PositionType.RIGHT, 1, 1)
sys_grid.attach_next_to(sysinfo, users_b, gtk.PositionType.RIGHT, 1, 1)
