
import AXUI.logger as logger

import UIA
import win32
import Translater

LOGGER = logger.get_logger()

class UIElementException(Exception):
    pass


class Method(object):
    '''
    UIA Method wrapper
    '''
    def __init__(self, UIA_method_object, *args):
        self.UIA_method = UIA_method_object
        self.args = args
        
    def __call__(self):
        

class Pattern(object):
    '''
    UIA pattern wapper
    '''
    def __init__(self, UIA_pattern_instance):
        self.UIA_pattern = UIA_pattern_instance
        
    def _get_method(self, method_name):
        
        
    def _get_all_methods(self):
    
    
    def _call_method(self, method_name, *args):
    
    
    def __getattr__(self, name):
    
        

class CoordinateElement(UIElement):
    '''
    coordinate element is for coordinate identifier
    functions are limited, only support keyboard, mouse and touch operation
    '''
    def __init__(self, coordinate):
        self.coordinate = coordinate
    
    def find(self, parsed_identifier):
        #TODO maybe we should let coordinate element have children
        raise UIElementException("coordinate element should not have children")
    
    def verify(self):
        return self
    
    def get_property(self, name):
        raise UIElementException("coordinate element don't support property")
        
    def get_pattern(self, name):
        raise UIElementException("coordinate element don't support pattern")
        
    def _get_coordinate(self):
        return self.coordinate
                
    def __getattr__(self, name):
        if name == "keyboard":
            return self.get_keyboard()
        elif name == "mouse":
            return self.get_mouse()
        elif name == "touch":
            return self.get_touch()
        else:
            raise AttributeError("Attribute not exist: %s" % name)

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
        translated_identifier = Translater.ID_Translater(parsed_identifier)
        if translated_identifier[0] == "Coordinate":
            return CordinateElement(translated_identifier[1])
        elif translated_identifier[0] == "Index":
            return UIElement(self.UIAElement.FindAll(UIA.UIA_wrapper.TreeScope_Descendants, translated_identifier[1][0])[translated_identifier[1][1]])
        elif translated_identifier[0] == "UIA":
            return UIElement(self.UIAElement.FindFirst(UIA.UIA_wrapper.TreeScope_Descendants, translated_identifier[1]))
 
    def verify(self):
        '''
        verify UI element is still exist
        '''
        LOGGER.debug("UIElement verify")
        return UIElement(self.UIAElement.FindFirst(UIA.UIA_wrapper.TreeScope_Element, UIA.IUIAutomation.CreateTrueCondition()))
        
    def get_property(self, name):
        return UIA.get_property_by_id(self.UIAElement, name)
        
    def get_pattern(self, name):
        return UIA.get_pattern_by_id(self.UIAElement, name)
    
    def _get_coordinate(self):
        pass
    
    def get_keyboard(self):
        return win32.Keyboard(self._get_coordinate())
    
    def get_mouse(self):
        return win32.Mouse(self._get_coordinate())
    
    def get_touch(self):
        return win32.Touch(self._get_coordinate())
        
    def __getattr__(self, name):
        if name == "keyboard":
            return self.get_keyboard()
        elif name == "mouse":
            return self.get_mouse()
        elif name == "touch":
            return self.get_touch()
        elif name in UIA.UIA_property_identifers_mapping.keys():
            return self.get_property(name)
        elif name in UIA.UIA_Pattern_identifers_mapping.keys():
            return self.get_pattern(name)
        else:
            raise AttributeError("Attribute not exist: %s" % name)
        
class RootUIElement(UIElement):
    pass
