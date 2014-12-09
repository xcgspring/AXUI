
config_section="driver"
default_configs={ #"driver_used": "fake_driver",
                  "driver_used": "windows",
                }

DriverUsed = default_configs["driver_used"]

def config(configs=default_configs):
    '''callback function used by config module
    
    '''
    global DriverUsed
    DriverUsed=configs["driver_used"]

#used by config module
__all__=["config_section", "default_configs", "config"]
