
from AXUI.exceptions import DriverException

class Method(object):
    '''
    optional interface,
    this class is a method wrapper for UIElement methods, if UI API has native python lib, this class might not needed
    '''
    pass

class Pattern(object):
    '''
    optional interface,
    this class is a method set for different kinds of UIElement
    usually different kind of UIElements support different set of methods
    we can assign different pattern for these UIElements
    '''
    pass

class UIElement(object):
    '''This class defines interfaces for common UI element
    
    Every driver (Windows, Appium, Selenium) should implement this interfaces,
    provides independent interfaces for uplevel modules, so we transplant AXUI cross different platform
    
    Attributes:
        find_element:           find the first descendant element which matches parsed_identifier
        find_elements:          find all elements which match parsed_identifier
        verify:                 verify current element is valid

        get_keyboard:           class for keyboard related methods
        get_mouse:              class for mouse related methods
        get_touch:              class for touch related methods
        
        get_property:           get property value for current element
        get_pattern:            get pattern interface for current element
    '''
    def find_element(self, parsed_identifier):
        '''
        find the first child UI element via identifier, return one UIAElement if success, return None if not find
        '''
        raise NotImplementedError("Not implement")
        
    def find_elements(self, parsed_identifier):
        '''
        find the child UI elements via identifier, return a list containing target UI elements
        '''
        raise NotImplementedError("Not implement")
        
    def get_property(self, name):
        '''
        get property value
        '''
        raise NotImplementedError("Not implement")
        
    def get_pattern(self, name):
        '''
        pattern is a class support one kind of UI actions
        '''
        raise NotImplementedError("Not implement")
        
    def get_keyboard(self):
        '''
        get keyboard class to use keyboard related methods
        '''
        raise NotImplementedError("Not implement")
    
    def get_mouse(self):
        '''
        get mouse class to use mouse related methods
        '''
        raise NotImplementedError("Not implement")
    
    def get_touch(self):
        '''
        get touch class to use touch related methods
        '''
        raise NotImplementedError("Not implement")
        
    def __getattr__(self, name):
        if name == "Keyboard":
            return self.get_keyboard()
        elif name == "Mouse":
            return self.get_mouse()
        elif name == "Touch":
            return self.get_touch()
        else:
            attr = self.get_property(name)
            if attr is not None:
                return attr
            attr = self.get_pattern(name)
            if attr is not None:
                return attr   
            raise AttributeError("Attribute not exist: %s" % name)
            
class Root(UIElement):
    '''
    root is the entry point to interact with UI
    like desktop of windows UIA, web browser of web driver API
    
    This class defines interfaces for root element
    
    Every driver (Windows, Appium, Selenium) should implement this interfaces,
    provides independent interfaces for uplevel modules, so we transplant AXUI cross different platform
    
    Attributes:
        start:                  start root element
        stop:                   stop root element
        screenshot:             take a screen shot for root element
    
        find_element:           find the first descendant element which matches parsed_identifier
        find_elements:          find all elements which match parsed_identifier
        verify:                 verify current element is valid

        get_keyboard:           class for keyboard related methods
        get_mouse:              class for mouse related methods
        get_touch:              class for touch related methods
        
        get_property:           get property value for current element
        get_pattern:            get pattern interface for current element
    '''
    def start(self, **kwargs):
        '''
        get root ready
        like get root element in windows UIA, get browser to target website
        '''
        raise NotImplementedError("Not implement")
        
    def stop(self, **kwargs):
        '''
        stop root
        like close browser for web driver API
        '''
        raise NotImplementedError("Not implement")
        
    def screenshot(self, absfile_path):
        '''
        take a screen shot for root
        '''
        raise NotImplementedError("Not implement")