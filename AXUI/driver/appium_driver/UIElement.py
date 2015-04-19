
import re
import inspect

from AXUI.logger import LOGGER
from AXUI.driver import DriverException

try:
    import appium.webdriver as webdriver
except ImportError, e:
    LOGGER().error("To use AXUI appium driver, you must install selenium and appium python client first, check https://pypi.python.org/pypi/selenium, https://pypi.python.org/pypi/Appium-Python-Client")
    raise e

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import Translater

class Keyboard(object):
    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def input(self, *values):
        '''send keyboard input to UI element

        Keyboard input string:
        (1) For normal charactors like [0~9][a~z][A~Z], input directly
        (2) For special charactors like "space", "tab", "newline", "F1~F12"
            You use {key_name} to replace them, all support keys in "selenium/webdriver/common/keys "
        '''
        translated_values = []
        for value in values:
            #still support selenium Keys object
            if isinstance(value, Keys):
                translated_values.append(value)
            elif isinstance(value, int):
                translated_values.append(str(value))
            elif isinstance(value, str):
                #handle special keys
                if re.match("^{.*}$", value) != None:
                    key = value.lstrip("{").rstrip("}")
                    try:
                        key_value = getattr(Keys, key)
                    except AttributeError, e:
                        LOGGER().warning("Input special key not support: %s, skip this input" , key)
                    else:
                        translated_values.append(key_value)
                else:
                    translated_values.append(value)

        self.selenium_element.send_keys(*translated_values)

class Mouse(object):
    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def left_click(self):
        self.selenium_element.click()

class Touch(object):
    def __init__(self, selenium_element):
        self.selenium_element = selenium_element
		
	############################
	#porting appium touch methods
	############################
	def scroll(self, origin_el, destination_el):
		self.selenium_element.scroll(origin_el.selenium_element, destination_el.selenium_element)
		
	def drag_and_drop(self, origin_el, destination_el):
		self.selenium_element.drag_and_drop(origin_el.selenium_element, destination_el.selenium_element)
		
	def tap(self, positions, duration=None):
		self.selenium_element.tap(positions, duration)
		
	def swipe(self, start_x, start_y, end_x, end_y, duration=None):
		self.selenium_element.swipe(start_x, start_y, end_x, end_y, duration)
		
	def flick(self, start_x, start_y, end_x, end_y):
		self.selenium_element.flick(start_x, start_y, end_x, end_y)
		
	def pinch(self, element=None, percent=200, steps=50):
		self.selenium_element.pinch(element.selenium_element, percent, steps)
		
	def zoom(self, element=None, percent=200, steps=50):
		self.selenium_element.zoom(element.selenium_element, percent, steps)

class NormalPattern(object):
    '''
    pattern interface for browser
    '''
    interfaces = [
        "submit",
        "clear",

        "is_selected",
        "is_enabled",
        "is_displayed",

        "value_of_css_property",
    ]

    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def __getattr__(self, name):
        if name in self.interfaces:
            return getattr(self.selenium_element, name)
        else:
            LOGGER().info("This method not exist in NormalPattern: %s", name)

class BrowserPattern(object):
    '''
    pattern interface for browser
    '''
    interfaces = [
        "get",
        "close",
        "maximize_window",

        "execute_script",
        "execute_async_script",
        "set_script_timeout",

        "back",
        "forward",
        "refresh",

        "get_cookies",
        "get_cookie",
        "delete_cookie",
        "delete_all_cookies",
        "add_cookie",

        "implicitly_wait",
        "set_page_load_timeout",

        "set_window_size",
        "get_window_size",
        "set_window_position",
        "get_window_position",

        "get_log",
    ]

    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def __getattr__(self, name):
        if name in self.interfaces:
            return getattr(self.selenium_element, name)
        else:
            LOGGER().info("This method not exist in BrowserPattern: %s", name)
            
class MobilePattern(object):
    '''
    pattern interface for mobile root element
    '''
    #interfaces may change due to appium interface maybe change
    interfaces = [
    
        "scroll",
        "drag_and_drop",
        "tap",
        "swipe",
        "flick",
        "pinch",
        "zoom",
        
        "reset",
        
        "pull_file",
        "pull_folder",
        "push_file",
        
        "background_app",
        "is_app_installed",
        "install_app",
        "remove_app",
        "launch_app",
        "close_app",
        
        "start_activity",
        
        "lock",
        "shake",
        "open_notifications",
        "set_network_connection",
        
        "is_ime_active",
        "activate_ime_engine",
        "deactivate_ime_engine",
        
        "get_settings",
        "update_settings",
        
        "toggle_location_services",

    ]
    
    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def __getattr__(self, name):
        if name in self.interfaces:
            return getattr(self.selenium_element, name)
        else:
            LOGGER().info("This method not exist in MobileRootPattern: %s", name)
            
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

    def __init__(self, selenium_element):
        self.selenium_element = selenium_element

    def find_element(self, parsed_identifier):
        '''
        find the first child UI element via identifier, return one UIAElement if success, return None if not find
        '''
        translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()
        try:
            selenium_element = self.selenium_element.find_element(by=translated_identifier[0], value=translated_identifier[1])
        except NoSuchElementException:
            LOGGER().debug("Cannot find target element")
            return None
        else:
            return UIElement(selenium_element)

    def find_elements(self, parsed_identifier):
        '''
        find the child UI elements via identifier, return a list containing target UI elements
        '''
        translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()
        elements = self.selenium_element.find_elements(by=translated_identifier[0], value=translated_identifier[1])

        UIElements = []
        for element in elements:
            UIElements.append(UIElement(element))

        return UIElements

    def get_property(self, name):
        '''
        get property value
        '''
        try:
            obj = getattr(self.selenium_element, name)
        except AttributeError:
            LOGGER().debug("Cannot find this attribute: %s" , name)
            if hasattr(self.selenium_element, "get_attribute"):
                LOGGER().debug("Try get_attribute method")
                return self.selenium_element.get_attribute(name)
        else:
            if inspect.ismethod(obj):
                LOGGER().info("This is a method, not a property: %s" , name)
                return None
            else:
                return obj

    def get_pattern(self, name):
        '''
        pattern is a class support one kind of UI actions
        '''
        if name == "WebUIElementPattern":
            return NormalPattern(self.selenium_element)
        else:
            return None

    def get_keyboard(self):
        '''
        get keyboard class to use keyboard related methods
        '''
        return Keyboard(self.selenium_element)

    def get_mouse(self):
        '''
        get mouse class to use mouse related methods
        '''
        return Mouse(self.selenium_element)

    def get_touch(self):
        '''
        get touch class to use touch related methods
        '''
        return Touch(self.selenium_element)

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

    def __init__(self):
        self.webdriver = None

    @property
    def selenium_element(self):
        return self.webdriver

    def start(self, **kwargs):
        '''
        get root ready
        like get root element in windows UIA, get browser to target website

        must have a "browser_name" argument in kwargs to indicate which browser to use
        other kwargs are same as normal selenium webdrivers
        '''
        if "command_executor" not in kwargs:
            #use default command executor
            kwargs["command_executor"] = 'http://127.0.0.1:4444/wd/hub'

        self.webdriver = webdriver.Remote(**kwargs)

    def stop(self, **kwargs):
        '''
        stop root
        like close browser for web driver API
        '''
        self.webdriver.quit()

    def screenshot(self, absfile_path):
        '''
        take a screen shot for root
        '''
        self.webdriver.get_screenshot_as_file(absfile_path)
        
    def verify(self):
        '''
        verify if session exist, not check for appium
        '''
        return self.webdriver

    def get_pattern(self, name):
        '''
        pattern is a class support one kind of UI actions
        '''
        if name == "BrowserPattern":
            return BrowserPattern(self.selenium_element)
        elif name == "MobilePattern":
            return MobilePattern(self.selenium_element)
        else:
            return None

    def get_keyboard(self):
        '''
        get keyboard class to use keyboard related methods
        '''
        LOGGER().info("Browser not support keyboard action")
        return None

    def get_mouse(self):
        '''
        get mouse class to use mouse related methods
        '''
        LOGGER().info("Browser not support mouse action")
        return None

    def get_touch(self):
        '''
        get touch class to use touch related methods
        '''
        LOGGER().info("Browser not support touch action")
        return None