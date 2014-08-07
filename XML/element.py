#TODO
#1. Add UI bind function
#2. Add comments

import AXUI.config as AXUI_config
import AXUI.logger as AXUI_logger

class Element(object):
    '''
    '''
    def __init__(self, xml_element):
        self.attributes = {
            'ID':'',
            'name':'',
            'search_condition':'',
            'start_operation':'',
            'timeout':'',
            'if_validate':True,
            'reference_picture':''
        }
        self.parent = None
        self.children = []
        self.UIElement = None
        
        for attrib in self.attributes.items():
            attrib_key = attrib[0]
            attrib[attrib_key] = xml_element.attrib.get(attrib_key)

        for child_element in xml_element.findall("."):
            child = Element(child_element)
            child.parent = self
            self.children.append(child)

    def bind_UI_element(self):
        '''
        '''
            
    

    
