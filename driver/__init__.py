
import AXUI.logger as LOGGER
import AXUI.config as config
import config_driver

#TODO config driver here could make better
config.config_self()
config.config(config_driver)

driver_used = config_driver.DriverUsed
time_out = config_driver.TimeOut

try:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    driver = __import__(driver_used)
except ImportError:
    raise NotImplementedError("driver not implement: %s, check your driver folder" % driver_used)
    
UIElement = driver.UIElement
RootUIElement = driver.RootUIElement

