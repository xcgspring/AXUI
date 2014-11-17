
config_section="driver"
default_configs={ #"driver_used": "fake_driver",
                  "driver_used": "windows",
                  "timeout": 5,
                }

DriverUsed = default_configs["driver_used"]
TimeOut = default_configs["timeout"]

def config(configs=default_configs):
    '''callback function used by config module
    
    '''
    global DriverUsed
    global TimeOut
    DriverUsed=configs["driver_used"]
    TimeOut=configs["timeout"]

#used by config module
__all__=["config_section", "default_configs", "config"]
