import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

import scripts.menus.main_menu as mm

import scripts.menus.conns_menu as cnm
import scripts.menus.system_grid as sg
import scripts.menus.devices_menu as dm
import scripts.menus.appearance_menu as am
import scripts.menus.system.system_info as ssi
import scripts.menus.system.langNreg as lnr
import scripts.menus.system.dateNtime as dnt
import scripts.menus.system.users as usrs
import scripts.menus.appearance.font_grid as fntg
import scripts.menus.appearance.themes as thm
import scripts.menus.system.sounds as snds
import scripts.menus.system.power as pwr
import scripts.menus.devices.keyboard as kbd
import scripts.menus.devices.mouse as mse
import scripts.menus.devices.displays as dsp
import scripts.menus.appearance.desktop as dsk
import scripts.menus.connections.wifi as wifi
from scripts.iconsNconst import *



start_x = -1 * inc.win_w - 100
start_y = -1 * inc.win_h - 100

main_fixed = gtk.Fixed()

main_fixed.add(dsp.displays_fixed)
main_fixed.move(dsp.displays_fixed, start_x, start_y)

main_fixed.add(usrs.user_grid)
main_fixed.move(usrs.user_grid, start_x, start_y)

main_fixed.add(mse.mouse_grid)
main_fixed.move(mse.mouse_grid, start_x, start_y)

main_fixed.add(dsk.desktop_fixed)
main_fixed.move(dsk.desktop_fixed, start_x, start_y)

main_fixed.add(mm.main_menu)
main_fixed.move(mm.main_menu, 0, 0)

main_fixed.add(sg.sys_grid)
main_fixed.move(sg.sys_grid, start_x, start_y)

main_fixed.add(thm.themes_grid)
main_fixed.move(thm.themes_grid, start_x, start_y)

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

main_fixed.add(lnr.lnr_grid)
main_fixed.move(lnr.lnr_grid, start_x, start_y)

main_fixed.add(fntg.font_grid)
main_fixed.move(fntg.font_grid, start_x, start_y)

main_fixed.add(snds.sound_grid)
main_fixed.move(snds.sound_grid, start_x, start_y)

main_fixed.add(ssi.sysinfo_grid)
main_fixed.move(ssi.sysinfo_grid, start_x, start_y)

main_fixed.add(pwr.power_grid)
main_fixed.move(pwr.power_grid, start_x, start_y)

main_fixed.add(kbd.keyboard_grid)
main_fixed.move(kbd.keyboard_grid, start_x, start_y)
