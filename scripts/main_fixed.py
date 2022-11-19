import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

import scripts.menus.main_menu as mm

import scripts.menus.conns_menu as cnm
import scripts.menus.system_grid as sg
import scripts.menus.devices_menu as dm
import scripts.menus.appearance_menu as am
import scripts.menus.system.system_info as ssi

import scripts.menus.system.dateNtime as dnt

import scripts.menus.connections.wifi as wifi
from scripts.iconsNconst import *

start_x = -1 * inc.win_w - 100
start_y = -1 * inc.win_h - 100

main_fixed = gtk.Fixed()

main_fixed.add(mm.main_menu)
main_fixed.move(mm.main_menu, 0, 0)

main_fixed.add(sg.sys_grid)
main_fixed.move(sg.sys_grid, start_x, start_y)

main_fixed.add(cnm.conns_grid)
main_fixed.move(cnm.conns_grid, start_x, start_y)

main_fixed.add(dm.devices_menu)
main_fixed.move(dm.devices_menu, start_x, start_y)

main_fixed.add(am.appear_menu)
main_fixed.move(am.appear_menu, start_x, start_y)

main_fixed.add(dnt.dnt_grid)
main_fixed.move(dnt.dnt_grid, start_x, start_y)

main_fixed.add(wifi.wifi)
main_fixed.move(wifi.wifi, start_x, start_y)

main_fixed.add(ssi.sysinfo_grid)
main_fixed.move(ssi.sysinfo_grid, start_x, start_y)
