
import AXUI.logger as logger
import AXUI.config as config
import AXUI.XML.app_map as app_map

class UIOperations(object):
    '''
    '''
    def __init__(self):
        pass
        
    def load_app_map(self, app_map_xml):
        self.app_map = app_map.AppMap(app_map_xml)
        
    def open_(self, element):
        element = self.app_map.get_element(element)
        element.bind_UI_element()
        
        
    
        
