'''
translate AXUI identifier to Windows UIA searchCondition
'''
import re
import AXUI.logger as logger
import AXUI.parsing.identifier_parsing.identifier_parser as id_parser
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
    
#Custom identifiers is defined for UI elements not properly recongnized by UIA
#Custom identifiers used with UIA identifiers should its special rules
custom_identifiers=[
    #Custom UI element might not recongnized by UIA, we can use cordinate to simulate it
    #"Cordinate" should be used alone, used with other identifier will be skipped
    "Cordinate",
    #Find element by Index from a group of elements, you need check the Index before using this identifier
    #"Index" should used in top level "AND" relational identifiers, otherwise will be skipped 
    "Index"
    ]
    
#what we supprt to identify UI, used in the header of translated result
#to identify what technology used to identify the UI
supprted_identifiers=["UIA"].extend(custom_identifiers)

class TranslaterException(Exception):
    pass
    
class ParseException(TranslaterException):
    pass
    
class ID_Translater(object):
    '''
    translate string identifier to specify search condition
    '''
    def __init__(self):
        pass
        
    def get_parsed(self, str_identifier):
        '''
        get parsed result for raw identifier string
        '''
        parsed = id_parser.parse(str_identifier)
        if not parsed:
            raise ParseException("Identifier error, please check parser warning message to fix it")
        return parsed
        
    def _translated_atomic_identifier(self, parsed_atomic_id):
        if UIA_identifers_mapping.has_key(parsed_atomic_id):
            return IUIAutomation.CreatePropertyCondition(UIA_identifers_mapping[parsed_atomic_id[0]], parsed_atomic_id[1])
        else:
            #use no UIA identifier will be skipped
            return None
    
    def _translated_relational_identifier(self, relation, translated_id_1, translated_id_2):
        if relation == "AND":
            return IUIAutomation.CreateAndCondition(translated_id_1, translated_id_2)
        elif relation == "OR":
            return IUIAutomation.CreateOrCondition(translated_id_1, translated_id_2)
        else:
            raise TranslaterException("Get error relation id: %s" % repr(relation))
        
    def _translated_identifier(self, parsed_id)
        if len(parsed_id) == 3:
            translated_1 = self.translated_identifier(parsed[1])
            translated_2 = self.translated_identifier(parsed[2])
            if translated_1 and translated_2:
                translated = self._translated_relational_identifier(parsed_id, translated_id_1, translated_id_2)
            elif not translated_1 and translated_2:
                translated = translated_2
            elif translated_1 and not translated_2:
                translated = translated_1
            else:
                translated = None
        elif len(parsed_id) == 2:
            translated = self._translated_atomic_identifier(parsed_id)
        else:
            raise TranslaterException("Get error parsed_id: %s" % repr(parsed_id))
            
        LOGGER.debug("Get translated: %s" % repr(translated))
        return translated
        
    def translated_top_level_identifier(self, parsed_id):
        '''
        get tanslated result from parsed identifier
        '''
        #handle custom identifier here
        if len(parsed_id) == 2 and parsed_id[0] == "Cordinate":
            #handle "Cordinate" identifier
            return parsed_id
        elif len(parsed_id) == 3 and parsed_id[0] == "AND" and (parsed_id[1][0] == "Index" or parsed_id[2][0] == "Index")
            #handle "Index" identifier
            if parsed_id[1][0] == "Index":
                return ("Index", (self._translated_identifier(parsed_id[2]), parsed_id[1][1]))
            else:
                return ("Index", (self._translated_identifier(parsed_id[1]), parsed_id[2][1]))
        else:
            return ("UIA", self._translated_identifier(parsed_id))
        
    def get_translated(self, str_identifier):
        '''
        get translated result from identifier string
        '''
        return self.translated_top_level_identifier(self.get_parsed(str_identifier))
        

        
