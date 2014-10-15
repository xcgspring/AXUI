import os
import AXUI.logger as AXUI_logger

LOGGER = AXUI_logger.get_logger()

config_section="driver"
default_configs={ "driver_used": "windows",
                  "timeout": 5,
                }

DriverUsed = default_configs["driver_used"]
TimeOut = default_configs["timeout"]

def config(configs=default_configs):
    '''
    call back function used by config module
    '''
    global Driver
    global TimeOut
    AppMapLocation=configs["driver_used"]
    SchemaLocation=configs["timeout"]


