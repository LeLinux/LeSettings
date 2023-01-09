import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

from scripts.iconsNconst import *
import scripts.go2 as g2
import json5 as json
import scripts.menus.system.langNreg as langNreg
import scripts.menus.system.dateNtime as dateNtime
import scripts.menus.main_menu as main_menu
import scripts.menus.system_grid as system_grid
import scripts.menus.system.langNreg as langNreg
import scripts.menus.system.dateNtime as dateNtime
import scripts.menus.devices_menu as devices_menu
import scripts.menus.appearance_menu as appear_menu

mar_start = inc.main_const_def / 10
mar_top = mar_start

def change_lang(cbt):
    with open("config.json", "r",  encoding = "UTF-8") as read_file:
        config = json.load(read_file)

    config["system"]["langNreg"]["language"] = cbt.get_active()
    with open("config.json", "w",  encoding = "UTF-8") as read_file:
        json.dump(config, read_file)
    langs = ["ru.json", "en.json"]
    loc = []
    with open("scripts/localization/" + langs[config["system"]["langNreg"]["language"]], "r",  encoding = "UTF-8") as locale:
        loc = json.load(locale)
    #main menu
    main_menu.system_b.set_label(loc["system"]["name"])
    main_menu.conns_b.set_label(loc["connections"]["name"])
    main_menu.devices_b.set_label(loc["devices"]["name"])
    main_menu.appearance_b.set_label(loc["appearance"]["name"])

    #system grid
    system_grid.langNreg.set_label(loc["system"]["langNreg"]["name"])
    system_grid.dateNtime.set_label(loc["system"]["dateNtime"]["name"])
    system_grid.users_b.set_label(loc["system"]["users"]["name"])
    system_grid.sysinfo.set_label(loc["system"]["sysinfo"]["name"])
    system_grid.sound_b.set_label(loc["system"]["sounds"]["name"])
    system_grid.power_b.set_label(loc["system"]["power"]["name"])

    #langNreg
    langNreg.lang_l.set_label(loc["system"]["langNreg"]["language"])
    langNreg.reg_l.set_label(loc["system"]["langNreg"]["region"])

    #dateNtime
    dateNtime.autotime_l.set_label(loc["system"]["dateNtime"]["auto_set_time"])
    dateNtime.time_l.set_label(loc["system"]["dateNtime"]["time"])
    dateNtime.time_format.set_label(loc["system"]["dateNtime"]["time_format"])
    dateNtime.autodate_l.set_label(loc["system"]["dateNtime"]["auto_set_date"])
    dateNtime.date_l.set_label(loc["system"]["dateNtime"]["date"])


    #devices
    devices_menu.displays_b.set_label(loc["devices"]["displays"]["name"])
    devices_menu.keyboard_b.set_label(loc["devices"]["keyboard"]["name"])
    devices_menu.mouse_b.set_label(loc["devices"]["mouse"]["name"])
    devices_menu.printers_b.set_label(loc["devices"]["printers"]["name"])

    #appearance
    appear_menu.multitask_b.set_label(loc["appearance"]["multitask"]["name"])
    appear_menu.themes_b.set_label(loc["appearance"]['themes']['name'])
    appear_menu.fonts_b.set_label(loc['appearance']['fonts']['name'])
    appear_menu.desktop_b.set_label(loc['appearance']['desktop']['name'])



lang_l = gtk.Label("Language")
lang_l.get_style_context().add_class("label")
lang_l.set_xalign(0)
lang_l.set_property("width-request", inc.main_const_def)
lang_l.set_margin_start(inc.win_w/3.2)
lang_l.set_margin_top(inc.win_h/3.2)

reg_l = gtk.Label("Region")
reg_l.get_style_context().add_class("label")
reg_l.set_xalign(0)
reg_l.set_property("width-request", inc.main_const_def)
reg_l.set_margin_start(inc.win_w/3.2)
reg_l.set_margin_top(inc.win_h*0.05)


lang_list = ["Русский", "Engish"]
langs_selector = gtk.ComboBoxText()
for i in lang_list:
    langs_selector.append_text(i)
langs_selector.set_margin_start(mar_start)
langs_selector.set_margin_top(inc.win_h/3.2)
langs_selector.set_active(0)
langs_selector.connect("changed", change_lang)



reg_list = ["Europe/Moscow", "USA/New-York"]
reg_selector = gtk.ComboBoxText()
for i in reg_list:
    reg_selector.append_text(i)
reg_selector.set_margin_start(mar_start)
reg_selector.set_margin_top(mar_top)



lnr_grid = gtk.Grid()
lnr_grid.add(lang_l)
lnr_grid.attach(lang_l, 1, 1, 0, 0)
lnr_grid.attach_next_to(langs_selector, lang_l, gtk.PositionType.RIGHT, 1, 1)
lnr_grid.attach_next_to(reg_l, lang_l, gtk.PositionType.BOTTOM, 1, 1)
lnr_grid.attach_next_to(reg_selector, reg_l, gtk.PositionType.RIGHT, 1, 1)
