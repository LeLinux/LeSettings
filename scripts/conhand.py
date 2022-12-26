def configurator():
    import scripts.menus.system.langNreg as langNreg
    config = config_s.read()
    config_s.close()
    print(config)
    if("$system" in config):
        config = config.split()
        for i in range(len(config)):
            print(i, config[i])
        langNreg.langs_selector.set_active(int(config[3]))
        langNreg.reg_selector.set_active(int(config[6]))
        dateNtime.autotime_switcher.set_state(int(config[10]))
        dateNtime.autodate_switcher.set_state(int(config[18]))
        dateNtime.time_format_selector.set_active(int(config[13]))
        
    else:
        pass
