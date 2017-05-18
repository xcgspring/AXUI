from .config_driver import driver_config
from AXUI.logger import LOGGER

def get_driver():
    '''get driver
    Return: return driver module selected in config
    '''
    try:
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        driver = __import__(driver_config.driver_used+"_driver")
    except ImportError as e:
        LOGGER.error("Driver load error: %s" % driver_config.driver_used)
        raise e
        
    return driver