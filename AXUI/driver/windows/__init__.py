#set DPI awareness for win8.1
from AXUI.logger import LOGGER
import subprocess
p = subprocess.Popen("wmic path win32_operatingsystem get version", stdout=subprocess.PIPE)
(stdout, stderr) = p.communicate()
windows_version = stdout.split()[1]
if int(windows_version.split(".")[0]) >= 6 and int(windows_version.split(".")[1]) >= 3:
    LOGGER().debug("Set DPI awareness for windows verison: %s" % windows_version)
    import ctypes
    shcore = ctypes.windll.shcore
    shcore.SetProcessDpiAwareness(2)
    
from UIElement import UIElement
