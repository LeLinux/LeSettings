import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns

main_const, main_top_mar = get_consts(4)

#main selector grid & components
system_b = gtk.Button(label = "System")
btns.set_button_data(system_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.system_b_icon)


conns_b = gtk.Button(label = "Connections")
btns.set_button_data(conns_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.conns_b_icon)

devices_b = gtk.Button(label = "Devices")
btns.set_button_data(devices_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.devices_b_icon)

appearance_b = gtk.Button(label = "Appearance")
btns.set_button_data(appearance_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.appearance_b_icon)
                    
main_menu = gtk.Grid()
main_menu.add(system_b)
main_menu.attach(system_b, 1, 0, 2, 1)
main_menu.attach_next_to(conns_b, system_b, gtk.PositionType.RIGHT, 1, 1)
main_menu.attach_next_to(devices_b, system_b, gtk.PositionType.BOTTOM, 1, 1)
main_menu.attach_next_to(appearance_b, devices_b, gtk.PositionType.RIGHT, 1, 1)
