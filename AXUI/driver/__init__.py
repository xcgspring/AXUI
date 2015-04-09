#for config use
from config_driver import *

def get_driver():
    '''get driver
    Return: return driver module selected in config
    '''
    import config_driver
    driver_used = config_driver.DriverUsed

    try:
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        driver = __import__(driver_used)
    except ImportError:
        raise NotImplementedError("driver not implement: %s, check your driver folder" % driver_used)
        
    return driver