import gi
from screeninfo import get_monitors
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

import scripts.menus.main_menu as mm
import scripts.menus.conns_menu as cnm
import scripts.menus.system_grid as sg


from scripts.iconsNconst import *


main_fixed = gtk.Fixed()
main_fixed.add(mm.main_menu)
main_fixed.move(mm.main_menu, 0, 0)
main_fixed.add(sg.sys_grid)
main_fixed.move(sg.sys_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)
main_fixed.add(cnm.conns_grid)
main_fixed.move(cnm.conns_grid, -1 * inc.win_w - 100, -1 * inc.win_h - 100)