
config_section="driver"
default_configs={ #"driver_used": "fake_driver",
                  "driver_used": "windows",
                }

DriverUsed = default_configs["driver_used"]

def config(configs=None):
    '''callback function used by config module
    
    '''
    if configs is None:
        configs = default_configs
    
    global DriverUsed
    DriverUsed=configs["driver_used"]

#used by config module
__all__=["config_section", "default_configs", "config"]
