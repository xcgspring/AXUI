#for config use
from config_driver import *

def get_UIElement():
    '''get driver UIElement
    Return: return UIElement from driver selected in config
    '''
    import config_driver
    driver_used = config_driver.DriverUsed

    try:
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        driver = __import__(driver_used)
    except ImportError:
        raise NotImplementedError("driver not implement: %s, check your driver folder" % driver_used)
        
    return driver.UIElement