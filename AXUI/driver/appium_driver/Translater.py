'''
translate AXUI identifier to webdriver search condition
'''
from AXUI.logger import LOGGER
from AXUI.driver import DriverException

from appium.webdriver.common.mobileby import MobileBy

class ID_Translater(object):
    '''
    translate parsed identifier to accordingly selenium find identifier
    '''
    def __init__(self, parsed_identifier):
        self.parsed_identifier = parsed_identifier

    def get_translated(self):
        '''
        get translated result from parsed identifier
        '''
        if len(self.parsed_identifier) == 2:
            name = self.parsed_identifier[0]
            value = self.parsed_identifier[1]
            try:
                getattr(MobileBy, name.upper())
            except AttributeError:
                LOGGER().error("identifier not support: %s" , name)
                raise DriverException("identifier not support: %s" % name)
            return getattr(MobileBy, name.upper()), value
        else:
            LOGGER().error("Get error parsed_id: %s" , repr(self.parsed_identifier))
            raise DriverException("Get error parsed_id: %s" % repr(self.parsed_identifier))




