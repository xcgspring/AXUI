
import time
from AXUI.logger import LOGGER
import AXUI.driver as driver
import XML_config

class TimeOutError(Exception):
    pass

class FakeUIElement(object):
    '''used for Elements without identifier
    ''' 
    def __repr__(self):
        return "Fake element, Use when there is no identifier for this element"
    
    def verify(self):
        return self

class Element(object):
    '''wrapper for UIElement
    hold informations from app map, and provide UIElement interface for app map
    
    Attributes:
        name:               Element's name, from XML
        parent_string:      Element's parent string, from XML
        identifier_string:  Identifier string, from XML
        timeout:            Time out for this element, from XML
        children:           children elements
        parent:             parent element
        start_func:         function to start this element
        stop_func:          function to stop this element
        identifier:         parsed identifier 
        
        UIElement:          driver interface for UIElement
        
        verify:             function to verify if self still exist
        find:               function to find children element
        start:              function to start this element
        stop:               function to stop this element

    '''
    #fake UI element is for elements without identifier 
    fake_UI_element = FakeUIElement()
    
    def __init__(self):
        #Need init by app map
        self.name = ""
        self.parent_string = ""
        self.identifier_string = ""
        self.timeout = XML_config.query_timeout()
        self.children = {}
        self.parent = None
        self.start_func = None
        self.stop_func = None
        self.identifier = None
        
        #UIElement is assigned automatically during runtime
        self.UIElement = None
        
    def __repr__(self):
        docstring = "Element for: %s\n" % self.name
        if self.verify() is None:
            docstring += "  UIElement not init or stopped for this Element\n"
        else:
            docstring += self.UIElement.__repr__()
            
        return docstring
        
    def verify(self):
        '''verify UIElement is valid or not
        return None if not valid
        '''
        if not self.UIElement is None:
            self.UIElement = self.UIElement.verify()

        return self.UIElement
        
    def find(self, identifier):
        '''find element by identifier
        identifier should already be parsed
        '''
        result = self.verify()
        if result is self.fake_UI_element:
            return self.parent.find(identifier)
        elif result is None:
            self.start()
        return self.UIElement.find(identifier)
        
    def _start(self):
        if not self.start_func is None:
            self.start_func.run()

    def start(self):
        '''start and find this UIElement
        first need to check if parent is exist, if not start the parent first
        '''
        if self.verify() is None:
            #check if root element
            if self.parent is None:
                #root element
                LOGGER().debug("Root element found: %s" % self.name)
                self.UIElement = driver.get_UIElement().get_root()
                return

            #check parent's UIElement
            if self.parent.verify() is None:
                self.parent.start()

            #check if element already exist
            if self.identifier:
                #root element should use special find
                print self.name
                print self.parent.name
                if self.parent.parent is None:
                    self.UIElement = self.parent.root_find(self.identifier)
                else:
                    self.UIElement = self.parent.find(self.identifier)

                if self.UIElement is None:
                    #run start func
                    if self.start_func:
                        self._start()
                    #keep finding the element by identifier, until found or timeout
                    start_time = time.time()
                    while True:
                        LOGGER().debug("Normal UIElement found: %s" % self.name)
                        if self.parent.parent is None:
                            self.UIElement = self.parent.root_find(self.identifier)
                        else:
                            self.UIElement = self.parent.find(self.identifier)
                            
                        if not self.UIElement is None:
                            break
                        
                        time.sleep(0.1)
                        current_time = time.time()
                        if current_time - start_time > self.timeout:
                            raise TimeOutError("time out encounter, during element:%s start" % self.name)
            else:
                #run start func
                if self.start_func:
                    self._start()
      
                LOGGER().debug("Fake UI element found: %s" % self.name)
                #if identifier is not specified, use a fake UIElement to replace UIElement
                self.UIElement = self.fake_UI_element
            
    def _stop(self):
        if not self.stop_func is None:
            self.stop_func.run()
    
    def stop(self):
        '''stop and verify this UIElement
        Need to stop all children first
        '''
        if not self.verify() is None:
            #stop all children
            for name in self.children:
                self.children[name].stop()
                
            #stop self
            if self.stop_func:
                self._stop()
                
            #keep verify the element, until not found or timeout
            start_time = time.time()
            while True:
                if self.identifier:
                    LOGGER().debug("Normal UIElement stop: %s" % self.name)
                    self.UIElement = self._verify()
                else:
                    LOGGER().debug("Fake UI element stop: %s" % self.name)
                    #if identifier is not specified, use a fake UIElement to replace UIElement
                    self.UIElement = None
                
                if self.UIElement is None:
                    break 

                time.sleep(0.1)
                current_time = time.time()
                if current_time - start_time > self.timeout:
                    raise TimeOutError("time out encounter, during element:%s stop" % self.name)

    def get_child_by_name(self, name):
        '''get child UIElement by name
        '''
        return self.children[name]
            
    def __getattr__(self, name):
        if self.children.has_key(name):
            return self.get_child_by_name(name)
        else:
            self.start()
            return getattr(self.UIElement, name)


