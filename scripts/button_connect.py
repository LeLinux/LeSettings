from scripts.menus import *
import scripts.go2 as g2

def btn_connect():
	main_menu.system_b.connect("clicked", g2.go2system)
	headbar.back2before_b.connect("clicked", g2.back2before)
	main_menu.conns_b.connect("clicked", g2.go2conns)
	main_menu.devices_b.connect("clicked", g2.go2devices)
	main_menu.appearance_b.connect("clicked", g2.go2appear)
