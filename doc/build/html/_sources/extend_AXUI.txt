.. _`extend AXUI`:

=========================
Extend AXUI
=========================

:Page Status: Development
:Last Reviewed: 

AXUI driver interface
=========================

AXUI is first developed for easy use of windows UIAutomation API, then restructure to add support for `WebDriver <http://www.w3.org/TR/webdriver/>`_ API used by ``selenium`` and ``appium``.
So if your UI automation is similar to windows UIAutomation API or `WebDriver <http://www.w3.org/TR/webdriver/>`_ API, it will be easy to add support for it in AXUI.

AXUI driver interface exposes some basic interface for used in other AXUI modules,

details interfaces definition is in ``driver/template/UIElement.py`` ::

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

Implement you own driver
=========================

Most of platforms already supported by AXUI built-in driver, anyway AXUI still open for new drivers.
You can refer to upper built-in drivers to write your driver.

.. note::

 Before you start to implement your own driver for your UI, always be sure you really need to do this
 
 For Custom UI, if your developers have provided you a command line back door to control the UI, you do not need to write your own UI driver.
