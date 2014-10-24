
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
    wrapper for UIElement
    hold infos from app map
    provide UIElement inferface for app map
    '''
    
    fake_UI_element = FakeUIElement()
    
    def __init__(self):
        #Need init by app map
        self.name = ""
        self.parent_string = ""
        self.identifier_string = ""
        
        self.children = {}
        self.parent = None
        self.start_func = None
        self.stop_func = None
        self.identifier = None
        
        self.UIElement = None
        
    def verify(self):
        '''
        verify UIElement is still valid
        '''
        if self.UIElement:
            result = self.UIElement.verify()
            if result:
                self.UIElement = result
            else:
                self.UIElement = None
                
        return self.UIElement
        
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
            raise ElementOperationFail("Find operation fail, either UI not exist or UI not start")
        
    def _start(self):
        '''
        start this UI
        '''
        if self.start_func not None:
            self.start_func.run()

    def start(self):
        '''
        start and find this UIElement
        '''
        if self.verify():
            LOGGER.debug("UI already start, skip start again")
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
                #if identifier is not specified, use a fake UIElement to replace UIElement
                self.UIElement = self.fake_UI_element
            
    def _stop(self):
        '''
        stop this UI
        '''
        if self.stop_func is not None:
            self.stop_func.run()
    
    def stop(self):
        '''
        stop and verify this UIElement
        '''
        if not self.verify():
            LOGGER.debug("UI not exist, skip stop")
            return
        else:
            if self.stop_func:
                self._stop()
                if not self.verify():
                    raise ElementOperationFail("Element stop fail")

    def get_child_by_name(self, name):
        '''
        get child UIElement
        '''
        return self.children[name]
            
    def __getattr__(self, name):
        if self.children.has_key(name):
            return self.get_child_by_name(name)
        else:
            return getattr(self.UIElement, name)


