from scripts.menus import *
import scripts.go2 as g2

def btn_connect():
	main_menu.system_b.connect("clicked", g2.go2system)
	headbar.back2before_b.connect("clicked", g2.back2before)