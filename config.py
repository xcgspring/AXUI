#TODO
#1. Add comments and tests

import ConfigParser

raw_parser = None

class ConfigException(Exception):
    pass

def config_self(config_file="global.cfg"):
    global raw_parser
    raw_parser = ConfigParser.RawConfigParser()
    raw_parser.read(config_file)

def config(module):
    global raw_parser
    if not raw_parser:
        raise ConfigException("Before config other module, need config config_module first")
    
    section = module.config_section
    configs = {}

    for config in module.default_configs.items():
        option = config[0]
        try:
            value = raw_parser.get(section, option)
            configs[option] = value
        except ConfigParser.NoOptionError:
            configs[option] = module.default_configs[option]
        except ConfigParser.NoSectionError:
            configs = module.default_configs
                
    module.config(configs)
    return configs

__all__=[config_self, config, ConfigException]

