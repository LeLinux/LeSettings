import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns


main_const, main_top_mar = get_consts(3)

wifi_b = gtk.Button(label = "Wi-Fi")
btns.set_button_data(wifi_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const/2,
                    inc.wifi_b_icon)


bluetooth_b = gtk.Button(label = "Bluetooth")
btns.set_button_data(bluetooth_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const/2,
                    inc.bluetooth_b_icon)

ethernet_b = gtk.Button(label = "Ethernet")
btns.set_button_data(ethernet_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const/2,
                    inc.ethernet_b_icon)

conns_grid = gtk.Grid()
conns_grid.add(wifi_b)
conns_grid.attach(wifi_b, 1, 0, 2, 1)
conns_grid.attach_next_to(bluetooth_b, wifi_b, gtk.PositionType.RIGHT, 1, 1)
conns_grid.attach_next_to(ethernet_b, bluetooth_b, gtk.PositionType.RIGHT, 1, 1)
