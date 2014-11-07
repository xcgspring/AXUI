
import os
import config
import logger
import XML
import driver

def Config(config_file=""):
    '''config the system
    Arguments:
        config_file: self defined config file, if not valid, will use default config file
    '''
    try:
        if not os.path.isfile(config_file):
            raise Exception()
    except:
        print("config_file not valid, use default config file")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "global.cfg")
        
    config.config_self(config_file)
    config.config(logger)
    config.config(XML)
    config.config(driver)

#port AppMap here
AppMap=XML.AppMap

__all__=["Config", "AppMap"]