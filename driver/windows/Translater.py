'''
translate AXUI identifier to Windows UIA searchCondition
'''
import re
import AXUI.logger as logger
import UIA.UIA_wrapper as UIA
import UIA.IUIAutomation_object as IUIAutomation

LOGGER = logger.get_logger()

#UIA Automation Element Property Identifiers
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx
#You can check element property using inspect.exe
#http://msdn.microsoft.com/en-us/library/windows/desktop/dd318521(v=vs.85).aspx
UIA_identifers_mapping = {
    "AcceleratorKey":   UIA.UIA_AcceleratorKeyPropertyId,
    "AccessKey":        UIA.UIA_AccessKeyPropertyId,
    "AriaProperties":   UIA.UIA_AriaPropertiesPropertyId,
    "AriaRole":         UIA.UIA_AriaRolePropertyId,
    "AutomationId":     UIA.UIA_AutomationIdPropertyId,
    "BoundingRectangle":UIA.UIA_BoundingRectanglePropertyId,
    "ClassName":        UIA.UIA_ClassNamePropertyId,
    "ClickablePoint":   UIA.UIA_ClickablePointPropertyId,
    "ControllerFor":    UIA.UIA_ControllerForPropertyId,
    "ControlType":      UIA.UIA_ControlTypePropertyId,
    "Culture":          UIA.UIA_CulturePropertyId,
    "DescribedBy":      UIA.UIA_DescribedByPropertyId,
    "FlowsFrom":        UIA.UIA_FlowsFromPropertyId,
    "FlowsTo":          UIA.UIA_FlowsToPropertyId,
    "FrameworkId":      UIA.UIA_FrameworkIdPropertyId,
    "HasKeyboardFocus": UIA.UIA_HasKeyboardFocusPropertyId,
    "HelpText":         UIA.UIA_HelpTextPropertyId,
    "IsContentElement": UIA.UIA_IsContentElementPropertyId,
    "IsControlElement": UIA.UIA_IsControlElementPropertyId,
    "IsDataValidForForm": UIA.UIA_IsDataValidForFormPropertyId,
    "IsEnabled":        UIA.UIA_IsEnabledPropertyId,
    "IsKeyboardFocusable":UIA.UIA_IsKeyboardFocusablePropertyId,
    "IsOffscreen":      UIA.UIA_IsOffscreenPropertyId,
    "IsPassword":       UIA.UIA_IsPasswordPropertyId,
    "IsPeripheral":     UIA.UIA_IsPeripheralPropertyId,
    "IsRequiredForForm":UIA.UIA_IsRequiredForFormPropertyId,
    "ItemStatus":       UIA.UIA_ItemStatusPropertyId,
    "ItemType":         UIA.UIA_ItemTypePropertyId,
    "LabeledBy":        UIA.UIA_LabeledByPropertyId,
    "LiveSetting":      UIA.UIA_LiveSettingPropertyId,
    "LocalizedControlType":UIA.UIA_LocalizedControlTypePropertyId,
    "Name":             UIA.UIA_NamePropertyId,
    "NativeWindowHandle":UIA.UIA_NativeWindowHandlePropertyId,
    "OptimizeForVisualContent":UIA.UIA_OptimizeForVisualContentPropertyId,
    "Orientation":      UIA.UIA_OrientationPropertyId,
    "ProcessId":        UIA.UIA_ProcessIdPropertyId,
    "ProviderDescription":UIA.UIA_ProviderDescriptionPropertyId,
    "RuntimeId":        UIA.UIA_RuntimeIdPropertyId
    }
    
#special indentifiers is defined for UI elements not properly recongnized by UIA
special_identifiers_mapping={
    #Custom UI element might not recongnized by UIA, we can use cordinate to simulate it
    "Cordinate":
    #Find element by Index from a group of elements, you need check the Index before using this identifier
    "Index":
    }

class TranslaterException(Exception):
    
    
class ParseException(TranslaterException):
    

class Translater(object):
    '''
    translate string identifier to UIA search condition
    '''
    def __init__(self, identifier):
        self.identifier = identifier
        
    def create_search_condition(self, basic_identifier):
        '''
        create an UIA property search condition based on basic identifier
        '''
        (identifier_name, identifier_content) = basic_identifier.split("=")
        UIA_identifier_name = UIA_identifers_mapping[identifier_name.strip()]
        identifier_content = identifier_content.strip()
        
        return IUIAutomation.CreatePropertyCondition(UIA_identifier_name, identifier_content)
        
    def _validate(self, identifier):
        '''
        define identifier format for windows UIA
        identifier should constracted by sub_identifier, relation operaters(AND, OR) and brackets
        minimum identifier should be like "identifier_name=content"
        identifier_name is predefined, use undefined name will trigger exception
        content need use quates when containing spaces
        '''
        #validate brackets is paired
        bracket_count=0
        for c in list(identifier):
            if c == "(":
                bracket_count+=1
            if c == ")":
                bracket_count-=1
                
        if not bracket_count == 0:
            raise ParseException("identifier has unpair brackets:\n %s" % identifier)
            
    def _handle_identifier_without_bracket(self, identifier):
        '''
        handle identifier without bracket
        '''
        string=""
        quote_count=0
        quote_string=""
        identifier_name=[]
        identifier_content=[]
        relations=[]
        for c in list(identifier):
            if c == "'":
                quote_count+=1
                if not quote_count%2:
                    
                
            if quote_count%2:
                quote_string="".join((quote_string, c))
            else:
                if quote_string:
                    identifier_content.append(quota_string.strip("'"))
                    quote_string=""
                else:
                    string="".join((quote_string, c))
                
            if c == "=":
                if string:
                    identifier_name.append(quota_string.strip())
                string=""
                
            match_result = re.match(".*AND.*|.*OR.*", string)

                
        
        
    def translate(self, identifier):
        '''
        translate indentifier to search condition
        '''
        bracket_count=0
        sub_conditions=[]
        relations=[]
        sub_identifier=""
        bracket_identifier=""
        for c in list(identifier):
            if c == "(":
                bracket_count+=1
            elif c == ")":
                bracket_count-=1

            if bracket_count < 0:
                raise ParseException("identifier has unpair brackets:\n %s" % identifier)
            elif bracket_count > 0:
                if sub_identifier:
                    #handle sub_identifier here
                    self._handle_identifier_without_bracket(sub_identifier)
                    sub_identifier=""
                else:
                    bracket_identifier="".join((bracket_identifier, c))
            elif bracket_count == 0:
                if bracket_identifier:
                    #handle bracket_identifier here
                    sub_conditions.append(self.translate(bracket_identifier.strip()))
                    bracket_identifier=""
                else:
                    sub_identifier="".join((sub_identifier, c))

        if bracket_count != 0:
            raise ParseException("identifier has unpair brackets:\n %s" % identifier)
        if sub_identifier:
            #handle rest sub_identifier here
            self._handle_identifier_without_bracket(sub_identifier)
        
        
        
        
