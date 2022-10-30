import gi
gi.require_version("Gtk", "3.0")

from scripts.iconsNconst import *
from scripts.menus import main_menu, system_grid, headbar, conns_menu, devices_menu, appearance_menu
from scripts.menus.system import dateNtime
from scripts.main_fixed import *

window = None
position = 0

def set_win_init(win):
    global window
    window = win

def go2system(btn):
    global window, position
    print("[LOG] GO2SYSTEM function started")
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(system_grid.sys_grid, 0, 0)
    position = 1
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)
    print("[LOG] GO2SYSTEM function finished")

def go2dateNtime(btn):
    global window, position
    position = 6
    main_fixed.move(dateNtime.dnt_grid, 0, 0)
    main_fixed.move(system_grid.sys_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)

def go2conns(btn):
    global window, position
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(conns_menu.conns_grid, 0, 0)
    position = 2
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)

def go2devices(btn):
    global window, position
    print("[LOG] GO2DEVICES function started")
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(devices_menu.devices_menu, 0, 0)
    position = 3
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)
    print("[LOG] GO2DEVICES function finished")

def go2appear(btn):
    global window, position
    print("[LOG] GO2APPEAR function started")
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(appearance_menu.appear_menu, 0, 0)
    position = 4
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)
    print("[LOG] GO2APPEAR function finished")


def go2menu(btn):
    global window, position
    print("[LOG] GO2MENU function started")
    if position == 1:
        main_fixed.move(system_grid.sys_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
        main_fixed.move(main_menu.main_menu, 0, 0)
    elif position == 2:
        main_fixed.move(conns_menu.conns_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
        main_fixed.move(main_menu.main_menu, 0, 0)
    elif position == 3:
        main_fixed.move(devices_menu.devices_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
        main_fixed.move(main_menu.main_menu, 0, 0)
    elif position == 4:
        main_fixed.move(appearance_menu.appear_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
        main_fixed.move(main_menu.main_menu, 0, 0)
    elif position == 5:
        pass
    elif position == 6:
        main_fixed.move(dateNtime.dnt_grid, -1 * inc.win_w -100, -1 *  inc.win_h - 100)
        main_fixed.move(system_grid.sys_grid, 0, 0)
    position = 0
    headbar.headb_fixed.move(headbar.back2before_b, -1 * inc.win_w, -1 * inc.win_h)
    print("[LOG] GO2MENU function finished")

def back2before(btn):
    global window, position
    if 1 <= position <= 4:
        go2menu(1)
