from gi.repository import Gtk as gtk

def set_button_data(btn, width, height, mar_top, mar_start, icon):
	btn.set_relief(gtk.ReliefStyle.NONE)
	btn.get_style_context().add_class("button")
	btn.set_image(icon)
	btn.set_image_position(gtk.PositionType.TOP)
	btn.set_use_underline(1)
	btn.set_always_show_image(1)
	btn.set_property("width-request", width)
	btn.set_property("height-request", height)
	btn.set_margin_top(mar_top)
	btn.set_margin_start(mar_start)

def set_label_data():
	pass
