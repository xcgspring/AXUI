
import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
import AXUI.parsing.identifier_parsing.identifier_parser as id_parser

import element
import func
import XML_config

LOGGER = AXUI_logger.get_logger()

class AppMapException(Exception):
    pass

class AppMap(object):
    '''
    represent a app map
    '''
    RootIdentifier = ""
    
    def __init__(self, xml):
        self.app_map_xml = XML_config.query_app_map_file(xml)
        self.elements = {}
        self.func_maps = {}
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
            self.elements[name] = AppMap(path)
        
    def _parse_include_func_element(self, root_element):
        for include_func_element in root_element.findall("AXUI:include_func", namespaces={"AXUI":"AXUI"}):
            name = include_func_element.attrib["name"]
            path = include_func_element.attrib["path"]
            self.func_maps[name] = func.FuncMap(path)

    def _init_element(self, xml_element):
        element = element.Element()

        element.name = xml_element.attrib["name"]
        if xml_element.attrib.has_key("start_func"):
            element.start_func = self.get_func_by_name(xml_element.attrib["start_func"])
        if xml_element.attrib.has_key("stop_func"):
            element.stop_func = self.get_func_by_name(xml_element.attrib["stop_func"])
        if xml_element.attrib.has_key("identifier"):
            element.identifier = id_parser.parse(xml_element.attrib["identifier"])
            
        return element

    def _build_element(self, xml_element, parent_element):
        element = self._init_element(xml_element)

        element.parent = parent_element
        parent_element.children[element.name] = element

    def _build_top_level_element(self, xml_element):
        element = self._init_element(xml_element)
            
        #top level element must have parent
        #except root element
        if element.parent_string:
            element.parent = self.get_element_by_name(element.parent_string)
        elif element.identifier == self.RootIdentifier
            element.parent = None
        else:
            raise AppMapException("Top level element except root must have parent, miss parent in element: %s" % element.name)

    def _build_elements(self, parent_xml_element, parent_element):  
        for xml_element in \
        parent_xml_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            element = self._build_element(xml_element)            
            self._build_elements(xml_element, element)

    def _parse_elements(self, root_element):
        for xml_element in \
        root_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            element = self._build_top_level_element(xml_element)                
            self.elements[element.name] = element
            self._build_UI_element_wrapper(xml_element, element)
            
    def parse_elements(self):
        '''
        parse all elements in the app map
        '''
        element_tree = ET.parse(self.app_map_xml)
        root_element = element_tree.getroot()
        
        self._parse_include_app_map_element(root_element)
        self._parse_include_func_element(root_element)
        self._parse_elements(root_element)

    def get_element_by_name(self, name_list):
        '''
        get element by name, name_list should be like "element1.element2...elementX"
        '''
        parent_element = self
        for name in name_list.split("."):
            element = getattr(parent_element, name)
            parent_element = element
        
        return element
        
    def get_func_by_name(self, func_name):
        '''
        get func by name, func name should be like "func_map_name.func_name"
        '''
        try:
            (func_map_name, func_name) = func_name.split(".")
            func_map = self.func_maps[func_map_name]
            return getattr(func_map, func_name)
        except ValueError, TypeError:
            raise ValueError("Func string error: %s. Should be like \"func_map_name.func_name\"" % name)
        
    def __getattr__(self, name):
        return self.elements[name]
        
