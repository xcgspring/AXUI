
import AXUI.logger as logger

import UIA.UIA_wrapper as UIA
import UIA.IUIAutomation_object as IUIAutomation
import UIA.UIA_property_identifers_mapping as UIA_property_identifers_mapping
import UIA.UIA_Pattern_identifers_mapping as UIA_Pattern_identifers_mapping

import Translater.ID_Translater as ID_Translater
import win32_event as win32

LOGGER = logger.get_logger()

class CordinateElement(object):
    

class UIElement(object):
    '''
    This class implement driver UIElement interface for used by other module
    '''
    def __init__(self, UIAElement):
        self.UIAElement = UIAElement
        LOGGER.debug("UIElement instance init: %s" % repr(self.UIAElement))

    def find(self, parsed_identifier):
        '''
        find the UI element via identifier, return one UIAElement if success, return None if not find
        '''
        LOGGER.debug("UIElement find")
        translated_identifier = ID_Translater(parsed_identifier)
        if translated_identifier[0] == "Cordinate":
            return CordinateElement(translated_identifier[1]):
        elif translated_identifier[0] == "Index":
            return UIElement(self.UIAElement.FindAll(UIA.TreeScope_Descendants, translated_identifier[1][0])[translated_identifier[1][1]])
        elif translated_identifier[0] == "UIA":
            return UIElement(self.UIAElement.FindFirst(UIA.TreeScope_Descendants, translated_identifier[1]))
 
    def verify(self):
        '''
        verify UI element is still exist
        '''
        LOGGER.debug("UIElement verify")
        return UIElement(self.UIAElement.FindFirst(UIA.TreeScope_Element, IUIAutomation.CreateTrueCondition()))
        
    def get_property(self, name):
        
    def get_pattern(self, name):
    
    def get_keyboard(self):
    
    def get_mouse(self):
    
    def get_touch(self):
        
    def __getattr__(self, name):
        if name == "keyboard":
            return self.get_keyboard()
        elif name == "mouse":
            return self.get_mouse()
        elif name == "touch":
            return self.get_touch()
        elif name in UIA_property_identifers_mapping.keys():
            return self.get_property(name)
        elif name in UIA_Pattern_identifers_mapping.keys():
            return self.get_pattern(name)
        else:
            raise AttributeError("Attribute not exist: %s" % name)
        
class RootUIElement(UIElement):
    pass
