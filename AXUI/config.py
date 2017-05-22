'''
config module
'''

import configparser

from .XML import core_config
from .driver import driver_config
from .image import image_config
from .logger import logger_config


class GlobalConfig(object):
    supported_sections = ["core", "driver", "image", "logger"]
    def load_config_file(self, config_file):
        raw_parser = configparser.RawConfigParser()
        raw_parser.read(config_file)

        for section in raw_parser.sections():
            if section in self.supported_sections:
                module = eval(section+"_config")
                for option in raw_parser.options(section):
                    if hasattr(module, option):
                        setattr(module, option, raw_parser.get(section, option))

    def __getattr__(self, item):
        if item in self.supported_sections:
            return eval(item+"_config")
        else:
            raise AttributeError("No config for %s" % item)

Config = GlobalConfig()