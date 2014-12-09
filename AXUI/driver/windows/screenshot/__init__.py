
import os
import subprocess
from AXUI.logger import LOGGER

def screenshot(filename, coordinate=None):
    '''screenshot for target UI area
    
    parameters:
        handle:      window handler for target UI
        filename:    screenshot filename, should be .bmp file
        coordinate:  (left, top, right, bottom) coordinate for target area
    '''
    current_dir = os.path.dirname(__file__)
    screenshot_app = os.path.join(current_dir, "screenshot.exe")
    
    if coordinate is None:
        cmd = '"%s" -f %s' % (screenshot_app, filename)
    else:
        cmd = '"%s" -f %s -l %s -t %s -r %s -b %s' %\
               (screenshot_app, filename, coordinate[0], coordinate[1], coordinate[2], coordinate[3])
        
    LOGGER().debug("screenshot command: %s" % cmd)
    process = subprocess.Popen(cmd)
    
    return process.wait()
    
