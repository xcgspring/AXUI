
import AXUI.logger as AXUI_logger
from AXUI.driver import UIElement, RootUIElement
LOGGER = AXUI_logger.get_logger()

class ElementOperationFail(Exception):
    pass

class FakeUIElement(object):
    '''
    use to replace UIElement in Element without identifier
    '''
    def verify(self):
        return self

class Element(object):
    '''
    wrapper for UI element
    '''
    
    fake_UI_element = FakeUIElement()
    
    def __init__(self):
        self.name = ""
        self.parent_string = ""
        self.identifier_string = ""
        
        self.children = {}
        self.parent = None
        self.start_func = None
        self.stop_func = None
        self.identifier = None
        
        self.UIElement = None
        
        LOGGER.debug("Element instance for: %s" % self.name)
        
    def verify(self):
        '''
        '''
        if self.UIAElement:
            result = self.UIAElement.verify()
            if result:
                self.UIAElement = result
            else:
                self.UIAElement = None
                
        return self.UIAElement
        
    def find(self, identifier):
        '''
        find element by identifier
        '''
        result = self.verify()
        if self.fake_UI_element == result:
            return self.parent.find(identifier)
        elif result:
            return self.UIElement.find(identifier)
        else:
            raise ElementOperationFail("Find operation fail, either UI changed or UI not start")
        
    def _start(self):
        '''
        '''
        start_func

    def start(self):
        '''
        '''
        if self.verify():
            return
        else:
            if self.start_func:
                self._start()
            else:
                if self.parent:
                    self.parent.start()
                else:
                    #root element
                    LOGGER.debug("Root element create: %s" % self.name)
                    self.UIElement = RootUIElement()
                
            if self.identifier:
                LOGGER.debug("Normal UI element create: %s" % self.name)
                self.UIElement = self.parent.find(self.identifier)
            else:
                LOGGER.debug("Fake UI element create: %s" % self.name)
                #if identifier is not specify, use a fake UIElement to replace UIElement
                self.UIElement = self.fake_UI_element
            
    def _stop(self):
        '''
        '''
        stop_func
    
    def stop(self):
        '''
        '''
        if not self.verify():
            return
        else:
            if self.stop_func:
                self._stop()
                if not self.verify():
                    raise ElementOperationFail("Element stop fail")

    def get_child_by_name(self, name):
        return self.children[name]
            
    def __getattr__(self, name):
        if self.children.has_key(name):
            return self.get_child_by_name(name)
        else:
            return getattr(self.UIElement, name)


