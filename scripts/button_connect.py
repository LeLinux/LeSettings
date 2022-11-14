from scripts.menus import *
import scripts.go2 as g2

def btn_connect():
	headbar.back2menu.connect("clicked", g2.go2menu)
	headbar.back2system.connect("clicked", g2.go2system)

	main_menu.system_b.connect("clicked", g2.go2system)
	system_grid.dateNtime.connect("clicked", g2.go2dateNtime)

	main_menu.conns_b.connect("clicked", g2.go2conns)
	main_menu.devices_b.connect("clicked", g2.go2devices)
	main_menu.appearance_b.connect("clicked", g2.go2appear)
