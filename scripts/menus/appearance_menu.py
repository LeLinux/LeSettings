import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import scripts.button_settings as btns


main_const, main_top_mar = get_consts(4)

multitask_b = gtk.Button(label = "Multitasking")
btns.set_button_data(multitask_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.multitask_b_icon)

themes_b = gtk.Button(label = "Themes")
btns.set_button_data(themes_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.themes_b_icon)

fonts_b = gtk.Button(label = "Fonts")
btns.set_button_data(fonts_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.fonts_b_icon)

desktop_b = gtk.Button(label = "Desktop")
btns.set_button_data(desktop_b,
                    main_const,
                    main_const,
                    main_top_mar,
                    main_const,
                    inc.desktop_b_icon)

appear_menu = gtk.Grid()
appear_menu.add(multitask_b)
appear_menu.attach(multitask_b, 1, 0, 2, 1)
appear_menu.attach_next_to(themes_b, multitask_b, gtk.PositionType.RIGHT, 1, 1)
appear_menu.attach_next_to(fonts_b, multitask_b, gtk.PositionType.BOTTOM, 1, 1)
appear_menu.attach_next_to(desktop_b, fonts_b, gtk.PositionType.RIGHT, 1, 2)
