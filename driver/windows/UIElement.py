#TODO
#1. implement the operations
#2. make UIA and win32 import shorter

import AXUI.logger as logger
import AXUI.parsing.identifier_parsing.identifier_parser as id_parser

import UIA.UIA_wrapper as UIA
import win32_event as win32
import Translater.ID_Translater as ID_Translater

LOGGER = logger.get_logger()

class FakeUIElement(object):
    '''
    This class is for "Cordinate" identifier UIElement
    '''

class UIElement(object):
    '''
    This class implement driver UIElement interface for used by other module
    '''
    def __init__(self, name, **kwargs):
        LOGGER.debug("UIElement instance init start: %s" % name)
        self.name = name
        #get all info you needed here 
        self.__dict__ = kwargs
        
        if not self._find():
            self._start()
            self._find()
        
        LOGGER.debug("UIElement instance init complete: %s" % name)

    def _start(self):
        '''
        start the UI, via start_cmd or start_func
        '''

    def _find(self):
        '''
        find the UI element via identifier, return one UIAElement if success, return None if not find
        '''
        parsed_identifier = id_parser.parse(identifier)
        translated_identifier = ID_Translater(parsed_identifier).get_translated()
        if 
            
        
    def stop(self):
        '''
        stop the UI, via stop_cmd or stop_func
        '''

    def __getattar__(self, name):
        '''
        get UI supported property or pattern
        '''
        
