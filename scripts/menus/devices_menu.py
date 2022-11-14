import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns


main_const, main_top_mar = get_consts(4)

displays_b = gtk.Button(label = "Displays")
btns.set_button_data(displays_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.displays_b_icon)

keyboard_b = gtk.Button(label = "Keyboard")
btns.set_button_data(keyboard_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.keyboard_b_icon)

mouse_b = gtk.Button(label = "Mouse")
btns.set_button_data(mouse_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.mouse_b_icon)

printers_b = gtk.Button(label = "Printers")
btns.set_button_data(printers_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.printers_b_icon)

devices_menu = gtk.Grid()
devices_menu.add(displays_b)
devices_menu.attach(displays_b, 1, 0, 2, 1)
devices_menu.attach_next_to(keyboard_b, displays_b, gtk.PositionType.RIGHT, 1, 1)
devices_menu.attach_next_to(mouse_b, displays_b, gtk.PositionType.BOTTOM, 1, 1)
devices_menu.attach_next_to(printers_b, mouse_b, gtk.PositionType.RIGHT, 1, 2)
