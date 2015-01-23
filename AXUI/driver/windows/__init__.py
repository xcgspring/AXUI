#set DPI awareness for win8.1 and win10
from AXUI.logger import LOGGER
import subprocess
p = subprocess.Popen("wmic path win32_operatingsystem get version", stdout=subprocess.PIPE)
(stdout, stderr) = p.communicate()
windows_version = stdout.split()[1]
LOGGER().debug("Windows verison: %s" % windows_version)
#need set DPI awareness for win8.1 and win10
if (int(windows_version.split(".")[0]) >= 6 and int(windows_version.split(".")[1]) >= 3) \
    or int(windows_version.split(".")[0]) >= 10:
    LOGGER().debug("Set DPI awareness for windows verison: %s" % windows_version)
    import ctypes
    shcore = ctypes.windll.shcore
    shcore.SetProcessDpiAwareness(2)
    
from UIElement import UIElement
