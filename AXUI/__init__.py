
import os
import config
import logger
import driver
import XML
import image

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
    config.config(image)

def assertIsValid(element, msg="element not valid"):
    '''check if element valid
    '''
    if element.verify() is None:
        raise AssertionError(msg)
    
#port AppMap here
AppMap=XML.AppMap

#port image_compare here
from image import image_compare

__all__=["Config", "assertIsValid", "AppMap", "image_compare"]
