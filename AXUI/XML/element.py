
import os
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
        self.screenshot_location = XML_config.query_screenshot_location()
        self.screenshot_on_failure = XML_config.query_screenshot_on_failure()
        self.children = {}
        self.parent = None
        self.start_func = None
        self.stop_func = None
        self.identifier = None
        
        #UIElement is assigned automatically during runtime
        self.UIElement = None
        
    def __repr__(self):
        docstring = "element instance for: %s" % self.name
        return docstring
        
    @property
    def details(self):
        '''return details of this element
        '''
        docstring = "Element details for: %s\n" % self.name
        
        docstring += "#"*24
        docstring += "\n"
        docstring += "  Parent: %s\n" % repr(self.parent)
        
        docstring += "#"*24
        docstring += "\n"
        docstring += "  Children:\n"
        for key in self.children:
            docstring += "    %s\n" % repr(self.children[key])
        
        docstring += "#"*24
        docstring += "\n"
        docstring += "  UIElement details:\n"
        
        if self.verify() is None:
            docstring += "    UIElement not init or stopped for this Element\n"
        else:
            docstring += self.UIElement.__repr__()
            
        return docstring
        
    def verify(self):
        '''verify UIElement is valid or not
        return None if not valid
        '''
        #root element
        if self.parent is None:
            self.UIElement = driver.get_UIElement().get_root()
        #other
        else:
            self.UIElement = self.parent.find(self.identifier)
                
        return self.UIElement
        
    def find(self, identifier):
        '''find element by identifier
        identifier should already be parsed
        '''
        result = self.start()
        if result is None:
            #LOGGER().warn("UIElement not set yet, cannot use find method")
            return None
        elif result is self.fake_UI_element:
            return self.parent.find(identifier)
        else:
            if self.parent is None:
                return self.UIElement.root_find(identifier)
            else:
                return self.UIElement.find(identifier)
        
    def _start(self):
        if not self.start_func is None:
            self.start_func.run()

    def start(self):
        '''start and find this UIElement
        '''
        if self.verify() is None:
            #check if root element
            if self.parent is None:
                #root element
                LOGGER().debug("Root element found: %s" % self.name)
                self.UIElement = driver.get_UIElement().get_root()
                return self.UIElement
                
            if self.identifier:
                #run start func
                if self.start_func:
                    self._start()
                #keep finding the element by identifier, until found or timeout
                start_time = time.time()
                while True:
                    LOGGER().debug("Normal UIElement found: %s" % self.name)
                    self.UIElement = self.verify()
                            
                    if not self.UIElement is None:
                        break
                        
                    time.sleep(0.1)
                    current_time = time.time()
                    if current_time - start_time > self.timeout:
                        #do a desktop screenshot here as required
                        if self.screenshot_on_failure:
                            #get root
                            element = self
                            parent = element.parent
                            while not parent is None:
                                element = parent
                                parent = element.parent
                            #screenshot
                            element.screenshot()
                            
                        raise TimeOutError("time out encounter, during element:%s start" % self.name)
            else:
                #run start func
                if self.start_func:
                    self._start()
      
                LOGGER().debug("Fake UI element found: %s" % self.name)
                #if identifier is not specified, use a fake UIElement to replace UIElement
                self.UIElement = self.fake_UI_element
                
        return self.UIElement
            
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
            #only stop and check element which has stop_func attribute
            if self.stop_func:
                self._stop()
                
                #keep verify the element, until not found or timeout
                start_time = time.time()
                while True:
                    if self.identifier:
                        LOGGER().debug("Normal UIElement stop: %s" % self.name)
                        self.UIElement = self.verify()
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

    def findall(self, identifier):
        '''find all elements match identifier
        '''
        self.start()
        if self.parent is None:
            children_UIElements = self.UIElement._root_find_all_by_UIA(identifier)
        else:
            children_UIElements = self.UIElement._find_all_by_UIA(identifier)
            
        return children_UIElements
        
    def screenshot(self):
        '''take a screen shot for this element
        '''
        self.start()
        
        filename = self.name+"_"+time.strftime("%y%m%d_%H%M%S")+".bmp"
        absfile = os.path.join(self.screenshot_location, filename)
        if os.path.isfile(absfile):
            os.remove(absfile)
            
        self.UIElement.screenshot(absfile)
        LOGGER().debug("screenshot take: %s" % absfile)
        return absfile

    def __getattr__(self, name):
        if self.children.has_key(name):
            return self.children[name] 
        else:
            self.start()
            return getattr(self.UIElement, name)

class ElementGroup(object):
    '''
    '''
    def __init__(self):
        #Need init by app map
        self.name = ""
        self.parent_string = ""
        self.identifier_string = ""
        #move this to config later
        self.timedelay = 2
        self.parent = None
        self.start_func = None
        self.stop_func = None
        self.identifier = None
        
        #Elements is assigned dynamicly during runtime
        self.Elements = []
        
    def __repr__(self):
        docstring = "elementgroup instance for: %s" % self.name
        return docstring
        
    def _start(self):
        if not self.start_func is None:
            self.start_func.run()

    def start(self):
        '''start and findall UIElements, build Elements automatically
        '''
        #run start func
        if self.start_func:
            self._start()
        #delay some time
        time.sleep(self.timedelay)
        #find and create all matched elements
        UIElements = self.parent.findall(self.identifier)
        
        for i, UIElement in enumerate(UIElements):
            element = Element()
            element.parent = self.parent
            if self.identifier is None:
                child_element.identifier = ["Index", i]
            else:
                child_element.identifier = ("AND", self.identifier, ("Index", i))
            element.UIElement = UIElement
            element.name = UIElement.Name
            
            self.Elements.append(child_element)
        
        return self.Elements
        
    def _stop(self):
        if not self.stop_func is None:
            self.stop_func.run()
    
    def stop(self):
        '''stop this Element group 
        '''
        #stop self
        #only stop element which has stop_func attribute
        if self.stop_func:
            self._stop()
        
    def __getitem__(self, index):
        self.start()
        return self.Elements[index]
        
    def __iter__(self):
        self.start()
        return iter(self.Elements)
        
    def __len__(self):
        self.start()
        return len(self.Elements)
