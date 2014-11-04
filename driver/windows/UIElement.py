
import AXUI.logger as AXUI_logger

import UIA
import win32
import ctypes

import Translater

LOGGER = AXUI_logger.get_logger()

class UIElementException(Exception):
    pass
    
def _unpack(flag, name, *args):
    return flag, name, args

class Method(object):
    def __init__(self, function_object, name, args_expected=[]):
        self.function_object = funtion_object
        self.name = name
        self.args = []
        self.outs = []
        for arg in args_expected:
            arg_direction = arg[0]
            arg_type = arg[1]
            arg_name = arg[2]
            if arg_direction == "in":
                self.args.append([arg_type, arg_name])
            elif arg_direction == "out":
                self.outs.append([arg_type, arg_name])
            else:
                #skip unsupport arg_direction
                LOGGER.warn("Unsupport arg_direction: %s" % arg_direction)
                continue
        
    def __repr__(self):
        docstring += "Name:\t"+self.name+"\n"
        argument_string = "Arguments:\n"
        for argument in self.args:
            argument_type = argument[0]
            argument_name = argument[1]

            if argument_type == "POINTER(IUIAutomationElement)":
                argument_type = "UIElement"
            elif argument_type in UIA.UIA_enums:
                argument_type = UIA.UIA_enums[argument_type]
                        
            argument_string +="\tName:\t"+argument_name+"\n"
            argument_string +="\tType:\t"+repr(argument_type)+"\n\n"
        
        return_string = "Return:\n"
        for out in self.outs:
            return_name = out[0]
            return_type = out[1]
            return_string +="\tName:\t"+argument_name+"\n"
            return_string +="\tType:\t"+argument_type+"\n\n"
                    
        docstring += argument_string
        docstring += return_string
        
        return docstring
        
    def __call__(self, *args):
        '''
        For output value, use original value
        For input arguments:
            1. If required argument is an enum, check if input argument fit requirement
            2. If required argument is "POINTER(IUIAutomationElement)", we accept UIElement object,
               get required pointer object from UIElement, and send it to function
            3. Other, no change
        '''
        if len(self.args) != len(args):
            LOGGER.warn("Input arguments number not match expected")
            return None
        for index, expected_arg in enumerate(self.args):
            expected_arg_type = expected_arg[0]
            if expected_arg_type == "POINTER(IUIAutomationElement)":
                #get the UIAElment
                args[index] = args[index].UIAElement
            elif expected_arg_type in UIA.UIA_enums:
                #enum should be an int value, if argument is a string, should translate to int
                if args[index] in UIA.UIA_enums[expected_arg_type]:
                    args[index] = UIA.UIA_enums[expected_arg_type][args[index]]
                
                if args[index] not in UIA.UIA_enums[expected_arg_type].values():
                    LOGGER.warn("Input argument not in expected value: %s" % args[index])
                    return None
        
        return self.function_object(*args)

class Pattern(object):
    
    def __init__(self, UIAElement, pattern_identifier):
        self.UIAElement = UIAElement
        self.pattern_object = UIA.get_pattern_by_id(UIAElement, pattern_identifier)
        if self.pattern_object is None:
            raise UIElementException("Cannot get pattern, stop init pattern object")
        self.methods = {}
        self.properties = {}
        interface_description = UIA.UIA_control_pattern_interfaces[pattern_identifier]
        for member_description in interface_description:
            flag, name, args = _unpack(*member_description)
            #do a check, see if member exist in pattern object
            #if not, skip this member
            try:
                getattr(self.pattern_object, name)
            except AttributeError:
                LOGGER.warn("%s not exist in Pattern:%s"%(name, pattern_identifier))
                continue
                
            if flag == "method":
                self.methods[name] = args
            elif flag == "property":
                self.properties[name] = args
            else:
                raise UIElementException("Unrecongnized flag %s" % flag)
        
    def __repr__(self):
        docstring = ""
        docstring += "Properties:\n"
        for property_ in self.properties.items():
            name = property_[0]
            argument = property_[1][0]
            value_type = argument[1]
            value = getattr(self.pattern_object, name)
            docstring += "#"*32+"\n"
            docstring += "Name:\t"+name+"\n"
            docstring += "Value Type:\t"+value_type+"\n"
            docstring += "Value:\t"+repr(value)+"\n"
            
        docstring += "\nMethods:\n"
        for method_ in self.methods.items():
            name = method_[0]
            arguments = method_[1]
            docstring += "#"*32+"\n"
            docstring += "Name:\t"+name+"\n"
            argument_string = "Arguments:\n"
            return_string = "Return:\n"
            for argument in arguments:
                argument_direction = argument[0]
                argument_type = argument[1]
                argument_name = argument[2]

                if argument_direction == "in":
                    if argument_type == "POINTER(IUIAutomationElement)":
                        argument_type = "UIElement"
                    elif argument_type in UIA.UIA_enums:
                        argument_type = UIA.UIA_enums[argument_type]
                        
                    argument_string +="\tName:\t"+argument_name+"\n"
                    argument_string +="\tType:\t"+repr(argument_type)+"\n\n"
                elif argument_direction == "out":
                    return_string +="\tName:\t"+argument_name+"\n"
                    return_string +="\tType:\t"+argument_type+"\n\n"
                    
            docstring += argument_string
            docstring += return_string
            
        return docstring

    def __getattr__(self, name):
        member_object = getattr(self.pattern_object, name)
        if name in self.methods:
            return Method(member_object, name, self.methods[name])
        elif name in self.properties:
            return member_object
        else:
            raise AttributeError("Attribute not exist: %s" % name)
    
class UIElement(object):
    '''This class defines interfaces of UI element, basic unit of UI automation 
    
    Every driver (Windows, Android, Selenium) should implement these interfaces,
    provides independent interfaces for uplevel modules, so we transplant AXUI cross different platform
    
    Attributes:
        get_root:   class method, get the root element
        find:       find the first descendant element which matches parsed_identifier
        verify:     verify current UI element still exist
        keyboard:   get keyboard attached with this UI element
        mouse:      get mouse attached with this UI element
        touch:      get touch attached with this UI element
        other attributes:      get other attributes or interfaces supported by this UI element
    '''
    @classmethod
    def get_root(cls):
        return UIElement(UIA.IUIAutomation_object.GetRootElement())
    
    def __init__(self, UIAElement):
        #UIAElement is a pointer to IUIAutomation
        #
        self.UIAElement = UIAElement
        LOGGER.debug("UIElement instance init: %s" % repr(self.UIAElement))

    def __repr__(self):
        docstring = ""
        #generate UIA automation element properties
        docstring += "UIA automation element properties:\n"
        for identifier in UIA.UIA_automation_element_property_identifers:
            value = UIA.get_property_by_id(identifier)
            if value is not None:
                docstring += "%s:\t%s\n" % (identifier, repr(value))
                
        docstring += "\n\n"
        #generate UIA control pattern availability properties
        docstring += "UIA control pattern availability properties:\n"
        for identifier in UIA.UIA_control_pattern_availability_property_identifiers:
            value = UIA.get_property_by_id(identifier)
            if value is not None:
                docstring += "%s:\t%s\n" % (identifier, repr(value))
                
        return docstring

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
        UIAElement = self.UIAElement.FindFirst(UIA.UIA_wrapper.TreeScope_Element, UIA.IUIAutomation.CreateTrueCondition())
        return UIElement(UIAElement)
        
    def get_property(self, name):
        return UIA.get_property_by_id(self.UIAElement, name)
        
    def get_pattern(self, name):
        try:
            pattern = Pattern(name)
        except ValueError:
            pattern = None
            
        return pattern
    
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
        else:
            attr = self.get_property(name)
            if attr is not None:
                return attr
            attr = self.get_pattern(name)
            if attr is not None:
                return attr   
            raise AttributeError("Attribute not exist: %s" % name)


class CoordinateElement(UIElement):
    '''
    coordinate element is for coordinate identifier
    functions are limited, only support keyboard, mouse and touch operation
    '''
    def __init__(self, coordinate):
        self.coordinate = coordinate
    
    def __repr__(self):
        docstring = ""
    
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

