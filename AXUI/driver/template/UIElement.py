
class Method(object):
    '''
    this class is a method wrapper for UIElement methods, if UI API has native python lib, this class might not needed
    '''
    pass

class Pattern(object):
    '''
    this class is a method set for different kinds of UIElement
    usually different kind of UIElements support different set of methods
    we can assign different pattern for these UIElements
    '''
    pass

class UIElement(object):
    '''
    this is a template driver module need to implement
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

    def verify(self):
        '''
        verify UI element is still exist
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
        if name == "keyboard":
            return self.get_keyboard()
        elif name == "mouse":
            return self.get_mouse()
        elif name == "touch":
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
    '''
    def get(self, **kwargs):
        '''
        dynamic get root ready
        like get root element in windows UIA, get browser to target website
        '''
        raise NotImplementedError("Not implement")