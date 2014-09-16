
import AXUI.logger as logger
import AXUI.config as config
import AXUI.XML.app_map as app_map

class UIOperations(object):
    '''
    '''
    def __init__(self, app_map_xml):
        self.app_map_xml = app_map_xml
        self._load_app_map()
        
    def _load_app_map(self):
        self.app_map = app_map.AppMap(app_map_xml)
        
    def execute(self, cmd):
        (element_name, operation) = cmd.split()
        element = self.app_map.get_element_by_name(element_name)
        element.execute(operation)
    
    def execute_cmd_file(self, cmd_file):
        '''
        '''
        pass
        
    
        
