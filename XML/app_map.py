
import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
import func
import XML_config

LOGGER = AXUI_logger.get_logger()

class ElementWrapper(object):
    '''
    wrapper for UI element
    '''
    def __init__(self, xml_element):
        self.parent = None
        self.start_func = None
        try:
            self.start_cmd = xml_element.attrib["start_cmd"]
        except KeyError:
            self.start_cmd = None
        try:
            self.identifier = xml_element.attrib["identifier"]
        except KeyError:
            self.identifier= None
        self.UI_element = None
        self.xml_element = xml_element
            
    def parse_identifier(self):
        '''
        '''
        pass
        
    def bind_UI_element(self):
        '''
        bind this element to according UI element
        '''
        pass
        
    def execute(self, cmd):
        '''
        execute cmd with this element
        '''
        if self.UI_element:
            self.UI_element.execute(cmd)
        else:
            self.bind_UI_element()

class AppMap(object):
    '''
    represent a app map
    '''
    def __init__(self, xml):
        self.app_map_xml = XML_config.query_app_map_file(xml)
        self.elements = {}
        self.funcs = {}
        self.verification()
        self.parse_elements()

    def verification(self):
        '''
        verify the app map xml using according schema, need pyxb module
        '''
        try:
            import pyxb
        except ImportError:
            LOGGER.info("pyxb not install, skip app map verification")
            return
            
        from validate import check_app_map
        check_app_map(XML_config.query_schema_file("AXUI_app_map.xsd"), self.app_map_xml)

    def _parse_include_app_map_element(self, root_element):
        for include_app_map_element in root_element.findall("AXUI:include_app_map", namespaces={"AXUI":"AXUI"}):
            name = include_app_map_element.attrib["name"]
            path = include_app_map_element.attrib["path"]
            self.elements[name] = AppMap(path).elements
        
    def _parse_include_func_element(self, root_element):
        for include_func_element in root_element.findall("AXUI:include_func", namespaces={"AXUI":"AXUI"}):
            name = include_func_element.attrib["name"]
            path = include_func_element.attrib["path"]
            self.funcs[name] = func.FuncMap(path).funcs

    def _build_UI_element_wrapper(self, element_wrapper):  
        for UI_element in element_wrapper.xml_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            name = UI_element.attrib["name"]
            UI_element_wrapper = ElementWrapper(UI_element)
            #get element parent
            try:
                parent_string = UI_element.attrib["parent"]
                elements = self.elements
                for key in parent_string.split("."):
                    elements = elements[key]
                UI_element_wrapper.parent = elements
            except KeyError:
                UI_element_wrapper.parent = element_wrapper
                
            #get element func
            try:
                func_string = UI_element.attrib["func"]
                funcs = self.funcs
                for key in func_string.split("."):
                    funcs = funcs[key]
                UI_element_wrapper.start_func = funcs
            except KeyError:
                UI_element_wrapper.start_func = None
                
            self.elements[name] = UI_element_wrapper
            self._build_UI_element_wrapper(UI_element_wrapper)

    def _parse_UI_element(self, root_element):
        for UI_element in root_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            UI_element_wrapper = ElementWrapper(UI_element)
            name = UI_element.attrib["name"]
            #get element parent
            try:
                parent_string = UI_element.attrib["parent"]
                elements = self.elements
                for key in parent_string.split("."):
                    elements = elements[key]
                UI_element_wrapper.parent = elements
            except KeyError:
                UI_element_wrapper.parent = None
                
            #get element func
            try:
                func_string = UI_element.attrib["func"]
                funcs = self.funcs
                for key in func_string.split("."):
                    funcs = funcs[key]
                UI_element_wrapper.start_func = funcs
            except KeyError:
                UI_element_wrapper.start_func = None
                
            self.elements[name] = UI_element_wrapper
            self._build_UI_element_wrapper(UI_element_wrapper)
            
    def parse_elements(self):
        '''
        parse all elements in the app map
        '''
        element_tree = ET.parse(self.app_map_xml)
        root_element = element_tree.getroot()
        
        self._parse_include_app_map_element(root_element)
        self._parse_include_func_element(root_element)
        self._parse_UI_element(root_element)

    def get_element_by_name(self, name):
        '''
        get element by name
        '''
        elements = self.elements
        for key in name.split("."):
            elements = elements[key]
        return elements
        
