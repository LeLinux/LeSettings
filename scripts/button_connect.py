from scripts.menus import *
import scripts.go2 as g2

def btn_connect():
	headbar.back2menu.connect("clicked", g2.go2menu)
	headbar.back2system.connect("clicked", g2.go2system)

	main_menu.system_b.connect("clicked", g2.go2system)
	system_grid.dateNtime.connect("clicked", g2.go2dateNtime)
	system_grid.sysinfo.connect("clicked", g2.go2sysinfo)
	system_grid.langNreg.connect("clicked", g2.go2langNreg)
	system_grid.sound_b.connect("clicked", g2.go2sound)

	appearance_menu.fonts_b.connect("clicked", g2.go2fonts)

	main_menu.conns_b.connect("clicked", g2.go2conns)
	main_menu.devices_b.connect("clicked", g2.go2devices)
	main_menu.appearance_b.connect("clicked", g2.go2appear)
	conns_menu.wifi_b.connect("clicked", g2.go2wifi)
	system_grid.power_b.connect("clicked", g2.go2power)

	devices_menu.keyboard_b.connect("clicked", g2.go2keyboard)
	devices_menu.mouse_b.connect("clicked", g2.go2mouse)
