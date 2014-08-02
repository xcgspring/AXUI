#TODO
#1. implement the operations
#2. make UIA and win32 import shorter

import AXUI.logger as logger
import AXUI.driver.windows.UIA.UIA.UIA as UIA
import AXUI.driver.windows.win32_event as win32

class UIElement(object):
    '''
    '''
    xml_element = None

    mouse = None
    keyboard = None
    touch = None
    hardware = None

    UIAElement = None

    def __init__(self, xml_element):
        '''
        '''
        self.xml_element = xml_element

        self.mouse = win32.mouse
        self.keyboard = win32.keyboard
        self.touch = win32.touch
        self.hardware = win32.hardware

    def check_UI(self):
        '''
        '''
        self.UIAElement = UIA.search(self.xml_element.searchCondition, self.xml_element.timeout)
        if self.UIAElement == None:
            return False
        else:
            return True

    def mouse_click(self):
        '''
        '''

    def keyboard_input(self):
        '''
        '''

    def touch(self):
        '''
        '''

    def hardware_event(self):
        '''
        '''

        
