from config_driver import driver_config

class DriverException(Exception):
    pass

def get_driver():
    '''get driver
    Return: return driver module selected in config
    '''
    try:
        import sys, os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        driver = __import__(driver_config.driver_used+"_driver")
    except ImportError:
        raise NotImplementedError("driver not implement: %s, check your driver folder" % driver_config.driver_used)
        
    return driver