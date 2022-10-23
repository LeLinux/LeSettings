import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2

main_const, main_top_mar = get_consts(3)

wifi_b = gtk.Button(label = "Wi-Fi")
wifi_b.set_relief(gtk.ReliefStyle.NONE)
wifi_b.set_property("width-request", main_const)
wifi_b.set_property("height-request", main_const)
wifi_b.set_margin_top(main_top_mar)
wifi_b.set_margin_start(main_const / 2)
wifi_b.set_image(inc.wifi_b_icon)
wifi_b.set_image_position(gtk.PositionType.TOP)
wifi_b.set_use_underline(1)
wifi_b.set_always_show_image(1)

bluetooth_b = gtk.Button(label = "Bluetooth")
bluetooth_b.set_relief(gtk.ReliefStyle.NONE)
bluetooth_b.set_property("width-request", main_const)
bluetooth_b.set_property("height-request", main_const)
bluetooth_b.set_margin_top(main_top_mar)
bluetooth_b.set_margin_start(main_const / 2)
bluetooth_b.set_image(inc.bluetooth_b_icon)
bluetooth_b.set_image_position(gtk.PositionType.TOP)
bluetooth_b.set_use_underline(1)
bluetooth_b.set_always_show_image(1)

ethernet_b = gtk.Button(label = "Ethernet")
ethernet_b.set_relief(gtk.ReliefStyle.NONE)
ethernet_b.set_property("width-request", main_const)
ethernet_b.set_property("height-request", main_const)
ethernet_b.set_margin_top(main_top_mar)
ethernet_b.set_margin_start(main_const / 2)
ethernet_b.set_image(inc.ethernet_b_icon)
ethernet_b.set_image_position(gtk.PositionType.TOP)
ethernet_b.set_use_underline(1)
ethernet_b.set_always_show_image(1)

conns_grid = gtk.Grid()
conns_grid.add(wifi_b)
conns_grid.attach(wifi_b, 1, 0, 2, 1)
conns_grid.attach_next_to(bluetooth_b, wifi_b, gtk.PositionType.RIGHT, 1, 1)
conns_grid.attach_next_to(ethernet_b, bluetooth_b, gtk.PositionType.RIGHT, 1, 1)