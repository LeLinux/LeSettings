import json5 as json
'''
config = {
    "system" : {
        "langNreg" : {
            "language" : 1,
            "region" : 0
        },
        "dateNtime" : {
            "auto_set_time" : 1,
            "time_format" : 0,
            "auto_set_date" : 1,
        }
    },
    "devices" : {
        "displays" : {},
        "keyboard" : {},
        "mouse" : {},
        "printers" : {}
    },
    "appearance" : {
        "multitask" : {},
        "themes" : {},
        "fonts" : {},
        "desktop" : {}
    }
}

with open("config.json", "w") as write_file:
    json.dump(config, write_file)
'''
"""
locale = {
    "system" : {
        "name" : "System",
        "langNreg" : {
            "name" : "Language & Region",
            "language" : "Language",
            "region" : "Region"
        },
        "dateNtime" : {
            "name" : "Date & Time",
            "auto_set_time" : "Automatic set time",
            "time" : "Time",
            "time_format" : "Time format",
            "auto_set_date" : "Automatic set date",
            "date" : "Date"
        }
    },
    "connections" : {
        "name" : "Connections",
        "wifi" : {
            "name" : "wifi"
        }
    },
    "devices" : {
        "name" : "Devices",
        "displays" : {
            "name" : "Displays"
        },
        "keyboard" : {
            "name" : "Keyboard"
        },
        "mouse" : {
            "name" : "Mouse"
        },
        "printers" : {
            "name" : "Printers"
        }
    },
    "appearance" : {
        "name" : "Appearance",
        "multitask" : {
            "name" : "Multitasking"
        },
        "themes" : {
            "name" : "Themes"
        },
        "fonts" : {
            "name" : "Fonts"
        },
        "desktop" : {
            "name" : "Desktop"
        }

    }

}
"""
locale = {
    "system" : {
        "name" : "System",
        "langNreg" : {
            "name" : "Language & Region",
            "language" : "Language",
            "region" : "Region"
        },
        "dateNtime" : {
            "name" : "Date & Time",
            "auto_set_time" : "Automatic set time",
            "time" : "Time",
            "time_format" : "Time format",
            "auto_set_date" : "Automatic set date",
            "date" : "Date"
        },
        "users" : {
            "name" : "Users"
        },
        "sysinfo" : {
            "name" : "System info"
        },
        "sounds" : {
            "name" : "Sound"
        },
        "power" : {
            "name" : "Power"
        }

    },
    "connections" : {
        "name" : "Connections",
        "wifi" : {
            "name" : "wifi"
        }
    },
    "devices" : {
        "name" : "Devices",
        "displays" : {
            "name" : "Displays"
        },
        "keyboard" : {
            "name" : "Keyboard"
        },
        "mouse" : {
            "name" : "Mouse"
        },
        "printers" : {
            "name" : "Printers"
        }
    },
    "appearance" : {
        "name" : "Appearance",
        "multitask" : {
            "name" : "Multitasking"
        },
        "themes" : {
            "name" : "Themes"
        },
        "fonts" : {
            "name" : "Fonts"
        },
        "desktop" : {
            "name" : "Desktop"
        }

    }

}

with open("en.json", "w", encoding = "UTF-8") as write_file:
    json.dump(locale, write_file)
