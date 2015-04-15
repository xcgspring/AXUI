'''
translate AXUI identifier to Windows UIA searchCondition
'''
import re
from AXUI.logger import LOGGER
from AXUI.driver import DriverException
import UIA

#Custom identifiers is defined for UI elements not properly recongnized by UIA
#Custom identifiers used with UIA identifiers should its special rules
custom_identifiers=[
    #Custom UI element might not recongnized by UIA, we can use cordinate to simulate it
    #"Coordinate" should be used alone, used with other identifier will be skipped
    "Coordinate",
    #Find element by Index from a group of elements, you need check the Index before using this identifier
    #"Index" should used in top level "AND" relational identifiers, otherwise will be skipped 
    "Index"
    ]
    
#what we supprt to identify UI, used in the header of translated result
#to identify what technology used to identify the UI
supprted_identifiers=["UIA"].extend(custom_identifiers)

class ID_Translater(object):
    '''
    translate parsed identifier to acoordingly search condition
    '''
    def __init__(self, parsed_identifier):
        self.parsed_identifier = parsed_identifier
        
    def _translated_atomic_identifier(self, parsed_atomic_id):
        if parsed_atomic_id[0] in UIA.UIA_automation_element_property_identifers_mapping:
            return UIA.IUIAutomation_object.CreatePropertyCondition(UIA.UIA_automation_element_property_identifers_mapping[parsed_atomic_id[0]], parsed_atomic_id[1])
        elif parsed_atomic_id[0] in UIA.UIA_control_pattern_property_identifiers_mapping:
            return UIA.IUIAutomation_object.CreatePropertyCondition(UIA.UIA_control_pattern_property_identifiers_mapping[parsed_atomic_id[0]], parsed_atomic_id[1])
        else:
            #use no UIA identifier will be skipped
            LOGGER().warn("identifier: %s not in UIA property maps" , parsed_atomic_id[0])
            return None
    
    def _translated_relational_identifier(self, relation, translated_id_1, translated_id_2):
        if relation == "AND":
            return UIA.IUIAutomation_object.CreateAndCondition(translated_id_1, translated_id_2)
        elif relation == "OR":
            return UIA.IUIAutomation_object.CreateOrCondition(translated_id_1, translated_id_2)
        else:
            raise DriverException("Get error relation id: %s" % repr(relation))
        
    def _translated_identifier(self, parsed_id):
        if len(parsed_id) == 3:
            translated_id_1 = self._translated_identifier(parsed_id[1])
            translated_id_2 = self._translated_identifier(parsed_id[2])
            if translated_id_1 and translated_id_2:
                translated = self._translated_relational_identifier(parsed_id[0], translated_id_1, translated_id_2)
            elif not translated_id_1 and translated_id_2:
                translated = translated_id_2
            elif translated_id_1 and not translated_id_2:
                translated = translated_id_1
            else:
                translated = None
        elif len(parsed_id) == 2:
            translated = self._translated_atomic_identifier(parsed_id)
        else:
            raise DriverException("Get error parsed_id: %s" % repr(parsed_id))
            
        #LOGGER().debug("Get translated: %s" % repr(translated))
        return translated
        
    def translated_top_level_identifier(self, parsed_id):
        '''
        get tanslated result from parsed identifier
        '''
        #handle custom identifier here
        if len(parsed_id) == 2 and parsed_id[0] == "Coordinate":
            #handle "Coordinate" identifier
            return parsed_id
        elif len(parsed_id) == 2 and parsed_id[0] == "Index":
            #handle "Index" identifier
            return parsed_id
        elif len(parsed_id) == 3 and parsed_id[0] == "AND" and (parsed_id[1][0] == "Index" or parsed_id[2][0] == "Index"):
            #handle "Index" identifier
            if parsed_id[1][0] == "Index":
                return ("Index", (self._translated_identifier(parsed_id[2]), parsed_id[1][1]))
            else:
                return ("Index", (self._translated_identifier(parsed_id[1]), parsed_id[2][1]))
        else:
            return ("UIA", self._translated_identifier(parsed_id))
        
    def get_translated(self):
        '''
        get translated result from parsed identifier
        '''
        return self.translated_top_level_identifier(self.parsed_identifier)
        

        
