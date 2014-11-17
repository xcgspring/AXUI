'''
config module used to configure modules with contents in a config file
Functions:
    config_self:        set the config file to use
    config:             config the module with contents from config file
'''
import ConfigParser

raw_parser = None

class ConfigException(Exception):
    pass

def config_self(config_file):
    global raw_parser
    raw_parser = ConfigParser.RawConfigParser()
    raw_parser.read(config_file)

def config(module):
    '''
    module needs to contain interfaces as below: 
        config_section:     config_section is a string represent the section string in config file
        default_configs:    default configs to use when config not specified by config file
        config:             true method to do the configuration
    '''
    if raw_parser is None:
        raise ConfigException("Before config other module, need config config_module first")
    
    section = module.config_section
    configs = {}

    for config in module.default_configs.items():
        option = config[0]
        try:
            value = raw_parser.get(section, option)
            if not value:
                raise ValueError("No value in section: %s, option: %s" %(section, option))
            configs[option] = value
        except ConfigParser.NoOptionError:
            configs[option] = module.default_configs[option]
        except ConfigParser.NoSectionError:
            configs = module.default_configs

    module.config(configs)
    return configs
