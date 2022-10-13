from screeninfo import get_monitors  

sc_w, sc_h = get_monitors()[0].width, get_monitors()[0].height #get monitors resolution
win_w, win_h, w_const, h_const = sc_w, sc_h, 0.417, 0.31275 #set default constants

#that IF-ELSE block do dynamic change of window size by use screen resolution

if sc_w <= 1920 and sc_h <= 1080:
    win_w, win_h = 800, 600
else:
    win_w, win_h = sc_w * 0.417, sc_w * 0.31275

window = None

def set_win_init(win):
    global window
    window = win

def go2system(btn):
    global window
    print("[LOG] GO2SYSTEM function started")
    window.main_fixed.move(window.selector_grid, -1 * win_w - 100, -1 * win_h - 100)
    window.main_fixed.move(window.sys_grid, 0, 0)
    print("[LOG] GO2SYSTEM function finished")

def go2menu(btn):
    global window
    print("[LOG] GO2MENU function started")
    window.main_fixed.move(window.selector_grid, 0, 0)
    window.main_fixed.move(window.sys_grid, -1 * win_w - 100, -1 * win_h - 100)
    print("[LOG] GO2MENU function finished")
