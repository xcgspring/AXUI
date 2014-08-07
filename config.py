#TODO
#1. Add comments and tests

import ConfigParser as parser

import AXUI.logger as logger

__all__=[CONFIG]

CONFIG = Config("global.cfg")

class Config(object):
    '''
    '''
    def __init__(self, config_file):
        self.config = parser.RawConfigParser()
        self.config.read(config_file)

    def _get(self, section, option):
        return self.config.get(section, option)

    def config_logging(self):
        section = "logging"
        configs = {}

        for config in logger.default_config.items():
            option = config[0]
            try:
                value = self._get(section, option)
                configs[option] = value
            except parser.NoOptionError:
                configs[option] = logger.default_configs[option]
            except parser.NoSectionError:
                configs = logger.default_configs
                
        logger.config_logger(configs)

    def config_global(self):

    def config_all(self):
