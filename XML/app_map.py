
import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
from  AXUI.parsing.command_parsing import command_parser as cd_parser
import element as element_module
import func
import XML_config

LOGGER = AXUI_logger.get_logger()

class AppMapException(Exception):
    pass

def singleton(class_):
    instances = {}
    def getinstance(xml, **kwargs):
        full_xml = XML_config.query_app_map_file(xml)
        if full_xml not in instances:
            instances[full_xml] = class_(full_xml, **kwargs)
        return instances[full_xml]
        
    return getinstance
    
@singleton
class AppMap(object):
    '''
    represent a app map
    '''
    #move this setting to driver module
    RootIdentifier = "Name='Desktop'"
    
    def __init__(self, xml, uplevel_app_map_xmls=[]):
        self.app_map_xml = xml
        #prevent recursive include
        uplevel_app_map_xmls.append(self.app_map_xml)
        self.uplevel_app_map_xmls = uplevel_app_map_xmls
        self.app_maps = {}
        self.funcs = {}
        self.UI_elements = {}
        #verify the app map using pyxb
        self.verification()
        #parse the app map and build objects in memory
        self.parse_all()

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
        
    def _parse_include_elements(self, root_element):
        include_root = root_element.find("AXUI:includes", namespaces={"AXUI":"AXUI"})
        if include_root is not None:
            for include_element in include_root.findall("AXUI:include", namespaces={"AXUI":"AXUI"}):
                name = include_element.attrib["name"]
                path = include_element.attrib["path"]
                #prevent recursive include
                if XML_config.query_app_map_file(path) in self.uplevel_app_map_xmls:
                    raise AppMapException("Recursive include for app map: %s" % XML_config.query_app_map_file(path))
                self.app_maps[name] = AppMap(path, uplevel_app_map_xmls=self.uplevel_app_map_xmls)
            
    def _parse_func_elements(self, root_element):
        func_root = root_element.find("AXUI:funcs", namespaces={"AXUI":"AXUI"})
        if func_root is not None:
            for func_element in func_root.findall("AXUI:func", namespaces={"AXUI":"AXUI"}):
                name = func_element.attrib["name"]
                self.funcs[name] = func.Func(func_element, self)

    def _init_UI_element(self, xml_element):
        UI_element = element_module.Element()

        UI_element.name = xml_element.attrib["name"]
        if xml_element.attrib.has_key("parent"):
            UI_element.parent_string = xml_element.attrib["parent"]
        if xml_element.attrib.has_key("start_func"):
            UI_element.start_func = self.get_func_by_name(xml_element.attrib["start_func"])
        if xml_element.attrib.has_key("stop_func"):
            UI_element.stop_func = self.get_func_by_name(xml_element.attrib["stop_func"])
        if xml_element.attrib.has_key("identifier"):
            UI_element.identifier_string = xml_element.attrib["identifier"]
            UI_element.identifier = identifier_parser.parse(UI_element.identifier_string, lexer=identifier_lexer)
            
        return UI_element

    def _build_UI_element(self, xml_element, parent_UI_element):
        UI_element = self._init_UI_element(xml_element)

        UI_element.parent = parent_UI_element
        parent_UI_element.children[UI_element.name] = UI_element
        
        return UI_element

    def _build_top_level_UI_element(self, xml_element):
        UI_element = self._init_UI_element(xml_element)

        #top level element must have parent
        #except root element
        if UI_element.parent_string:
            UI_element.parent = self.get_UI_element_by_name(UI_element.parent_string)
        elif UI_element.identifier_string == self.RootIdentifier:
            UI_element.parent = None
        else:
            raise AppMapException("Top level element except root must have parent, miss parent in element: %s" % UI_element.name)
        
        return UI_element

    def _build_children_UI_elements(self, parent_xml_element, parent_element):  
        for xml_element in \
        parent_xml_element.findall("AXUI:UI_element", namespaces={"AXUI":"AXUI"}):
            UI_element = self._build_UI_element(xml_element, parent_element)            
            self._build_children_UI_elements(xml_element, UI_element)

    def _parse_UI_elements(self, root_element):
        UI_element_root = root_element.find("AXUI:UI_elements", namespaces={"AXUI":"AXUI"})
        if UI_element_root is not None:
            for xml_element in \
            UI_element_root.findall("AXUI:UI_element", namespaces={"AXUI":"AXUI"}):
                UI_element = self._build_top_level_UI_element(xml_element)                
                self.UI_elements[UI_element.name] = UI_element
                self._build_children_UI_elements(xml_element, UI_element)
            
    def parse_all(self):
        '''
        parse all elements (app_maps, funcs, UI_elements) in the app map
        '''
        element_tree = ET.parse(self.app_map_xml)
        root_element = element_tree.getroot()
        
        self._parse_include_elements(root_element)
        self._parse_func_elements(root_element)
        self._parse_UI_elements(root_element)

    def _get_object_by_name_list(self, name_list):
        parent = self
        for name in name_list:
            object_ = getattr(parent, name)
            parent = object_
        
        return object_

    def get_include_app_map_by_name(self, name_list):
        '''
        get app_map by name list
        name_list should be like "app_map1.app_map2...app_mapX"
        '''
        object_ = self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, AppMap):
            raise AppMapException("Expect app map, get %s, please check your name and app map" % type(object_))

    def get_UI_element_by_name(self, name_list):
        '''
        get element by name
        name_list should be like "app_map1.app_map2...element1.element2...elementX"
        '''
        return self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, element_module.Element):
            raise AppMapException("Expect UI element, get %s, please check your name and app map" % type(object_))
        
    def get_func_by_name(self, name_list):
        '''
        get func by name
        name_list should be like "app_map1.app_map2...app_mapX...func_name"
        '''
        return self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, func.Func):
            raise AppMapException("Expect func, get %s, please check your name and app map" % type(object_))

    def execute(self, command):
        '''
        execute command
        command like "app_map1.app_map2...element1.element2...operation [parameter1 parameter2 ...]"
        '''
        (object_name_list, parameter_list) = cd_parser.parse(command)
        object_= self._get_object_by_name_list(object_name_list)
        object_(parameter_list)
        
    def __getattr__(self, name):
        '''
        get app_map attribute
        will query object from app_maps > UI_elements > funcs
        '''
        if name in self.app_maps:
            return_object = self.app_maps[name]
        elif name in self.UI_elements:
            return_object = self.UI_elements[name]
        elif name in self.funcs:
            return_object = self.funcs[name]
        else:
            raise AttributeError("App map: %s don't have attribute: %s" % (self.app_map_xml, name))
            
        return return_object
        
