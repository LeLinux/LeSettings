import gi
gi.require_version("Gtk", "3.0")

from scripts.iconsNconst import *
from scripts.menus import main_menu, system_grid, headbar, conns_menu
from scripts.main_fixed import *

window = None
position = 0

def set_win_init(win):
    global window
    window = win

def go2conns(btn):
    global window, position
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(conns_menu.conns_grid, 0, 0)
    position = 2
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)


def go2system(btn):
    global window, position
    print("[LOG] GO2SYSTEM function started")
    main_fixed.move(main_menu.main_menu, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    main_fixed.move(system_grid.sys_grid, 0, 0)
    position = 1
    headbar.headb_fixed.move(headbar.back2before_b, 0, 0)
    print("[LOG] GO2SYSTEM function finished")

def go2menu(btn):
    global window, position
    print("[LOG] GO2MENU function started")
    main_fixed.move(main_menu.main_menu, 0, 0)
    if 1 <= position <= 4:
        main_fixed.move(system_grid.sys_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
        main_fixed.move(conns_menu.conns_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
    position = 0
    headbar.headb_fixed.move(headbar.back2before_b, -1 * inc.win_w, -1 * inc.win_h)
    print("[LOG] GO2MENU function finished")

def back2before(btn):
    global window, position
    if 1 <= position <= 4:
        go2menu(1)