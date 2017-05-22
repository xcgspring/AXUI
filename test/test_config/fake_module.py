
config_section="fake_module"
default_configs={ "config1":"config_set1",
                  "config2":"config_set2",
                  "config3":"config_set3",
                }


def config(configs=default_configs):
    print(configs["config1"])
    print(configs["config2"])
    print(configs["config3"])
