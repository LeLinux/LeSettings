import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as Gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns
import scripts.lesetlib as lesetlib

os_name_l = gtk.Label("OS name")
os_name_l.get_style_context().add_class("label")
os_name_l.set_xalign(0)
os_name_l.set_property("width-request", inc.main_const_def)
os_name_l.set_margin_start(inc.win_w*0.1)
os_name_l.set_margin_top(inc.win_h*0.1)

ram_l = gtk.Label("RAM")
ram_l.get_style_context().add_class("label")
ram_l.set_xalign(0)
ram_l.set_property("width-request", inc.main_const_def)
ram_l.set_margin_start(inc.win_w*0.1)
ram_l.set_margin_top(inc.win_h*0.1)

rom_l = gtk.Label("ROM")
rom_l.get_style_context().add_class("label")
rom_l.set_xalign(0)
rom_l.set_property("width-request", inc.main_const_def)
rom_l.set_margin_start(inc.win_w*0.1)
rom_l.set_margin_top(inc.win_h*0.1)

cpu_l = gtk.Label("CPU")
cpu_l.get_style_context().add_class("label")
cpu_l.set_xalign(0)
cpu_l.set_property("width-request", inc.main_const_def)
cpu_l.set_margin_start(inc.win_w*0.1)
cpu_l.set_margin_top(inc.win_h*0.1)

gpu_l = gtk.Label("GPU")
gpu_l.get_style_context().add_class("label")
gpu_l.set_xalign(0)
gpu_l.set_property("width-request", inc.main_const_def)
gpu_l.set_margin_start(inc.win_w*0.1)
gpu_l.set_margin_top(inc.win_h*0.1)


os_name_l_data = gtk.Label("OS name")
os_name_l_data.get_style_context().add_class("label")
os_name_l_data.set_xalign(0)
os_name_l_data.set_property("width-request", inc.main_const_def)
os_name_l_data.set_margin_start(inc.win_w*0.1)
os_name_l_data.set_margin_top(inc.win_h*0.1)

ram_l_data = gtk.Label("RAM")
ram_l_data.get_style_context().add_class("label")
ram_l_data.set_xalign(0)
ram_l_data.set_property("width-request", inc.main_const_def)
ram_l_data.set_margin_start(inc.win_w*0.1)
ram_l_data.set_margin_top(inc.win_h*0.1)

rom_l_data = gtk.Label("ROM")
rom_l_data.get_style_context().add_class("label")
rom_l_data.set_xalign(0)
rom_l_data.set_property("width-request", inc.main_const_def)
rom_l_data.set_margin_start(inc.win_w*0.1)
rom_l_data.set_margin_top(inc.win_h*0.1)

cpu_l_data = gtk.Label("CPU")
cpu_l_data.get_style_context().add_class("label")
cpu_l_data.set_xalign(0)
cpu_l_data.set_property("width-request", inc.main_const_def)
cpu_l_data.set_margin_start(inc.win_w*0.1)
cpu_l_data.set_margin_top(inc.win_h*0.1)

gpu_l_data = gtk.Label("GPU")
gpu_l_data.get_style_context().add_class("label")
gpu_l_data.set_xalign(0)
gpu_l_data.set_property("width-request", inc.main_const_def)
gpu_l_data.set_margin_start(inc.win_w*0.1)
gpu_l_data.set_margin_top(inc.win_h*0.1)

sysinfo_grid = gtk.Grid()
sysinfo_grid.add(os_name_l)
sysinfo_grid.attach(os_name_l, 1, 1, 1, 1)
sysinfo_grid.attach_next_to(os_name_l_data, os_name_l, gtk.PositionType.RIGHT, 1, 1)
sysinfo_grid.attach_next_to(ram_l, os_name_l, gtk.PositionType.BOTTOM, 1, 1)
sysinfo_grid.attach_next_to(ram_l_data, ram_l, gtk.PositionType.RIGHT, 1, 1)
sysinfo_grid.attach_next_to(rom_l, ram_l, gtk.PositionType.BOTTOM, 1, 1)
sysinfo_grid.attach_next_to(rom_l_data, rom_l, gtk.PositionType.RIGHT, 1, 1)
sysinfo_grid.attach_next_to(cpu_l, rom_l, gtk.PositionType.BOTTOM, 1, 1)
sysinfo_grid.attach_next_to(cpu_l_data, cpu_l, gtk.PositionType.RIGHT, 1, 1)
sysinfo_grid.attach_next_to(gpu_l, cpu_l, gtk.PositionType.BOTTOM, 1, 1)
sysinfo_grid.attach_next_to(gpu_l_data, gpu_l, gtk.PositionType.RIGHT, 1, 1)
