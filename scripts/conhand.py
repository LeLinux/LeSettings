import json5 as json
import scripts.menus.system.langNreg as langNreg
import scripts.menus.system.dateNtime as dateNtime
import scripts.menus.main_menu as main_menu
import scripts.menus.system_grid as system_grid
import scripts.menus.system.langNreg as langNreg
import scripts.menus.system.dateNtime as dateNtime
import scripts.menus.devices_menu as devices_menu
import scripts.menus.appearance_menu as appear_menu
def configurator():

    with open("config.json", "r",  encoding = "UTF-8") as read_file:
        config = json.load(read_file)
    print(config)
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

    if("system" in config):
        langNreg.langs_selector.set_active(config["system"]["langNreg"]["language"])
        langNreg.reg_selector.set_active(config["system"]["langNreg"]["region"])
        dateNtime.autotime_switcher.set_state(config["system"]["dateNtime"]["auto_set_time"])
        dateNtime.autodate_switcher.set_state(config["system"]["dateNtime"]["auto_set_date"])
        dateNtime.time_format_selector.set_active(config["system"]["dateNtime"]["time_format"])

    else:
        pass
