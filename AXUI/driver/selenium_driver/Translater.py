'''
translate AXUI identifier to Windows UIA searchCondition
'''
from AXUI.logger import LOGGER
from AXUI.exceptions import DriverException

from selenium.webdriver.common.by import By

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
                getattr(By, name.upper())
            except AttributeError:
                LOGGER().error("identifier not support: %s" , name)
                raise DriverException("identifier not support: %s" % name)
            return getattr(By, name.upper()), value
        else:
            LOGGER().error("Get error parsed_id: %s" , repr(self.parsed_identifier))
            raise DriverException("Get error parsed_id: %s" % repr(self.parsed_identifier))




