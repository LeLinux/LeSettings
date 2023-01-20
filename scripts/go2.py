import gi
gi.require_version("Gtk", "3.0")

from scripts.iconsNconst import *
from scripts.menus import main_menu, system_grid, headbar, conns_menu, devices_menu, appearance_menu
from scripts.menus.system import dateNtime, system_info, langNreg, power
#import scripts.menus.system.sounds
from scripts.menus.appearance import font_grid
from scripts.menus.devices import keyboard, mouse
from scripts.main_fixed import *

import scripts.lesetlib as lsl

"""
    0 - main menu
    1 - system menu
    2 - connections menu
    3 - devices menu
    4 - appearance menu
    5 - language & region menu
    6 - date & time menu
"""

position = 0
hide_x = -1 * inc.win_w - 100
hide_y = -1 * inc.win_h - 100

def go2system(btn):
    global position
    print("[LOG] GO2SYSTEM function started")
    main_fixed.move(main_menu.main_menu, hide_x, hide_y)
    main_fixed.move(system_grid.sys_grid, 0, 0)
    if position == 5:
        main_fixed.move(lnr.lnr_grid, hide_x, hide_y)
    elif position == 6:
        main_fixed.move(dateNtime.dnt_grid, hide_x, hide_y)
    elif position == 7:
        main_fixed.move(snds.sound_grid, hide_x, hide_y)
    elif position == 8:
        main_fixed.move(power.power_grid, hide_x, hide_y)

    elif position == 9:
        pass
    elif position == 10:
        main_fixed.move(system_info.sysinfo_grid, hide_x, hide_y)
    position = 1
    headbar.headb_fixed.move(headbar.back2menu, 0, 0)
    headbar.headb_fixed.move(headbar.back2system, hide_x, hide_y)
    print("[LOG] GO2SYSTEM function finished")

def go2sound(btn):
    global position
    main_fixed.move(snds.sound_grid, 0, 0)
    main_fixed.move(system_grid.sys_grid, hide_x, hide_y)
    headbar.headb_fixed.move(headbar.back2system, 0, 0)
    headbar.headb_fixed.move(headbar.back2menu, hide_x, hide_y)
    position = 7

def go2power(btn):
    global position
    main_fixed.move(power.power_grid, 0, 0)
    main_fixed.move(system_grid.sys_grid, hide_x, hide_y)
    headbar.headb_fixed.move(headbar.back2system, 0, 0)
    headbar.headb_fixed.move(headbar.back2menu, hide_x, hide_y)
    position = 8


def go2sysinfo(btn):
    global position
    main_fixed.move(system_info.sysinfo_grid, 0, 0)
    main_fixed.move(system_grid.sys_grid, hide_x, hide_y)
    headbar.headb_fixed.move(headbar.back2system, 0, 0)
    headbar.headb_fixed.move(headbar.back2menu, hide_x, hide_y)
    system_data = lsl.get_sysinfo()
    system_info.os_name_l_data.set_text(system_data[0])
    system_info.ram_l_data.set_text(system_data[1] + " GB")
    system_info.cpu_l_data.set_text(system_data[2][:45])
    system_info.gpu_l_data.set_text(system_data[3])

    position = 10

def go2langNreg(btn):
    global position
    main_fixed.move(system_grid.sys_grid, hide_x,  hide_y)
    main_fixed.move(lnr.lnr_grid, 0, 0)
    headbar.headb_fixed.move(headbar.back2system, 0, 0)
    headbar.headb_fixed.move(headbar.back2menu, hide_x, hide_y)
    position = 5

def go2dateNtime(btn):
    global position
    main_fixed.move(dateNtime.dnt_grid, 0, 0)
    main_fixed.move(system_grid.sys_grid, hide_x, hide_y)
    headbar.headb_fixed.move(headbar.back2system, 0, 0)
    headbar.headb_fixed.move(headbar.back2menu, hide_x, hide_y)
    position = 6

def go2conns(btn):
    global position
    main_fixed.move(main_menu.main_menu, hide_x, hide_y)
    main_fixed.move(conns_menu.conns_grid, 0, 0)
    position = 2
    headbar.headb_fixed.move(headbar.back2menu, 0, 0)

def go2wifi(btn):
    global position
    main_fixed.move(wifi.wifi, 0, 0)
    main_fixed.move(conns_menu.conns_grid, hide_x, hide_y)
    position = 11

def go2devices(btn):
    global position
    print("[LOG] GO2DEVICES function started")
    main_fixed.move(main_menu.main_menu, hide_x, hide_y)
    main_fixed.move(devices_menu.devices_menu, 0, 0)
    position = 3
    headbar.headb_fixed.move(headbar.back2menu, 0, 0)
    print("[LOG] GO2DEVICES function finished")

def go2keyboard(btn):
    global position
    position = 15
    main_fixed.move(devices_menu.devices_menu, hide_x, hide_y)
    main_fixed.move(keyboard.keyboard_grid, 0, 0)


def go2appear(btn):
    global position
    print("[LOG] GO2APPEAR function started")
    main_fixed.move(main_menu.main_menu, hide_x, hide_y)
    main_fixed.move(appearance_menu.appear_menu, 0, 0)
    position = 4
    headbar.headb_fixed.move(headbar.back2menu, 0, 0)
    print("[LOG] GO2APPEAR function finished. Position = " + str(position))

def go2fonts(btn):
    global position
    print("[LOG] GO2FONTS function started")
    main_fixed.move(font_grid.font_grid, 0, 0)
    main_fixed.move(appearance_menu.appear_menu, hide_x, hide_y)
    position = 20

def go2mouse(btn):
    global position
    main_fixed.move(devices_menu.devices_menu, hide_x, hide_y)
    main_fixed.move(mouse.mouse_grid, 0, 0)
    position = 16

def go2menu(btn):
    global position
    print("[LOG] GO2MENU function started")
    if position == 1:
        main_fixed.move(system_grid.sys_grid, hide_x, hide_y)
        print("[LOG] GO2MENU: system grid moved")
        main_fixed.move(main_menu.main_menu, 0, 0)
        headbar.headb_fixed.move(headbar.back2menu, -1 * inc.win_w, -1 * inc.win_h)
        position = 0
    elif position == 2:
        main_fixed.move(conns_menu.conns_grid, hide_x, hide_y)
        print("[LOG] GO2MENU: connections grid momar_topved")
        main_fixed.move(main_menu.main_menu, 0, 0)
        headbar.headb_fixed.move(headbar.back2menu, -1 * inc.win_w, -1 * inc.win_h)
        position = 0
    elif position == 3:
        main_fixed.move(devices_menu.devices_menu, hide_x, hide_y)
        print("[LOG] GO2MENU: devices_menu moved")
        main_fixed.move(main_menu.main_menu, 0, 0)
        headbar.headb_fixed.move(headbar.back2menu, -1 * inc.win_w, -1 * inc.win_h)
        position = 0
    elif position == 4:
        main_fixed.move(appearance_menu.appear_menu, hide_x, hide_y)
        print("[LOG] GO2MENU: appearance menu moved")
        main_fixed.move(main_menu.main_menu, 0, 0)
        headbar.headb_fixed.move(headbar.back2menu, -1 * inc.win_w, -1 * inc.win_h)
        position = 0
    if position == 11:
        main_fixed.move(wifi.wifi, hide_x, hide_y)
        main_fixed.move(conns_menu.conns_grid, 0, 0)
        position = 2
    if position == 20:
        main_fixed.move(font_grid.font_grid, hide_x, hide_y)
        main_fixed.move(appearance_menu.appear_menu, 0, 0)
        position = 4
    if position == 15:
        main_fixed.move(devices_menu.devices_menu, 0, 0)
        main_fixed.move(keyboard.keyboard_grid, hide_x, hide_y)
        position = 3
    if position == 16:
        main_fixed.move(devices_menu.devices_menu, 0, 0)
        main_fixed.move(mouse.mouse_grid, hide_x, hide_y)
        position = 3
    print("[LOG] GO2MENU function finished. Current position = " + str(position))
