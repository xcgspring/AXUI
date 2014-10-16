'''
translate AXUI identifier to Windows UIA searchCondition
'''
import re
import AXUI.logger as logger
import UIA.UIA_wrapper as UIA
import UIA.IUIAutomation_object as IUIAutomation
import UIA.UIA_identifers_mapping as UIA_identifers_mapping

LOGGER = logger.get_logger()

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
    
class ID_Translater(object):
    '''
    translate parsed identifier to specify search condition
    '''
    def __init__(self, parsed_identifier):
        self.parsed_identifier = parsed_identifier
        
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
        
    def get_translated(self):
        '''
        get translated result from parsed identifier
        '''
        return self.translated_top_level_identifier(self.parsed_identifier)
        

        
