

class UIElement(object):
    '''
    this is a template driver module need to implement
    '''
    property_keys = []
    pattern_keys = []
    def find(self, parsed_identifier):
        '''
        find the UI element via identifier, return one UIAElement if success, return None if not find
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
        get pattern supprted by UI element
        '''
        raise NotImplementedError("Not implement")
        
    def get_keyboard(self):
        '''
        get keyboard
        '''
        raise NotImplementedError("Not implement")
    
    def get_mouse(self):
        '''
        get mouse
        '''
        raise NotImplementedError("Not implement")
    
    def get_touch(self):
        '''
        get touch
        '''
        raise NotImplementedError("Not implement")
        
    def __getattr__(self, name):
        if name == "keyboard":
            return self.get_keyboard()
        elif name == "mouse":
            return self.get_mouse()
        elif name == "touch":
            return self.get_touch()
        elif name in self.property_keys:
            return self.get_property(name)
        elif name in self.pattern_keys:
            return self.get_pattern(name)
        else:
            raise AttributeError("Attribute not exist: %s" % name)
            
class RootUIElement(UIElement):
    '''
    represent root element
    '''
    pass
            
        
