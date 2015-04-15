import os
import re
import subprocess
import xml.etree.ElementTree as ET

from AXUI.logger import LOGGER
from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
from  AXUI.parsing.gui_command_parsing import gui_command_lexer, gui_command_parser
from  AXUI.parsing.cli_command_parsing import cli_command_lexer, cli_command_parser
import func
import XML_config
import element as element_module

def singleton(class_):
    instances = {}
    def getinstance(xml, **kwargs):
        full_xml = XML_config.query_app_map_file(xml)
        if full_xml not in instances:
            #uplevel_app_map_xmls is a global value in decorater
            #will overwrite it if there is argument passed in
            #if no argument passed in, set to [] manually
            if len(kwargs) == 0:
                instances[full_xml] = class_(full_xml, uplevel_app_map_xmls=[])
            else:
                instances[full_xml] = class_(full_xml, **kwargs)
        return instances[full_xml]
        
    return getinstance
    
@singleton
class AppMap(object):
    '''represent a app map
    one instance for one app map
    app map includes UI elements, functions and other app maps
    app maps should not recursive include each other
    '''
    
    def __init__(self, xml, uplevel_app_map_xmls):
        self.app_map_xml = xml
        #prevent recursive include
        uplevel_app_map_xmls.append(self.app_map_xml)
        self.uplevel_app_map_xmls = uplevel_app_map_xmls
        self.variables = {}
        self.app_maps = {}
        self.funcs = {}
        self.UI_elements = {}
        #verify the app map using pyxb
        self.verification()
        #parse the app map and build objects in memory
        self.parse_all()

    def __repr__(self):
        docstring = "AppMap:\n"
        docstring += "  Include Variables:\n"
        for variable in self.variables:
            docstring += "    %s: %s\n" % (variable, repr(self.variables[variable]))
        docstring += "  Include AppMaps:\n"
        for appmap in self.app_maps:
            docstring += "    %s\n" % appmap
        docstring += "  Include Functions:\n"
        for func_ in self.funcs:
            docstring += "    %s\n" % func_
        docstring += "  Include UI elements:\n"
        for element in self.UI_elements:
            docstring += "    %s\n" % element
        
        return docstring
        
    def verification(self):
        '''verify the app map xml using according schema, need pyxb module
        '''
        try:
            import pyxb
        except ImportError:
            LOGGER().info("pyxb not install, skip app map verification")
            return
            
        from validate import check_app_map
        check_app_map(XML_config.query_schema_file("AXUI_app_map.xsd"), self.app_map_xml)
        
    def _parse_variable_elements(self, root_element):
        variable_root = root_element.find("AXUI:variables", namespaces={"AXUI":"AXUI"})
        if variable_root is not None:
            for variable_element in variable_root.findall("AXUI:variable", namespaces={"AXUI":"AXUI"}):
                name = variable_element.attrib["name"]
                value = variable_element.attrib["value"]
                self.variables[name] = value
        
    def _parse_include_elements(self, root_element):
        include_root = root_element.find("AXUI:includes", namespaces={"AXUI":"AXUI"})
        if include_root is not None:
            for include_element in include_root.findall("AXUI:include", namespaces={"AXUI":"AXUI"}):
                name = include_element.attrib["name"]
                path = include_element.attrib["path"]
                #prevent recursive include
                if XML_config.query_app_map_file(path) in self.uplevel_app_map_xmls:
                    raise ValueError("Recursive include for app map: %s" % XML_config.query_app_map_file(path))
                self.app_maps[name] = AppMap(path, uplevel_app_map_xmls=self.uplevel_app_map_xmls)
            
    def _parse_func_elements(self, root_element):
        func_root = root_element.find("AXUI:funcs", namespaces={"AXUI":"AXUI"})
        if func_root is not None:
            for func_element in func_root.findall("AXUI:func", namespaces={"AXUI":"AXUI"}):
                name = func_element.attrib["name"]
                self.funcs[name] = func.Func(func_element, self)

    def _init_UI_element(self, xml_element):
        if xml_element.tag == "{AXUI}UI_element":
            UI_element = element_module.Element()
            
            UI_element.name = xml_element.attrib["name"]
            if "timeout" in xml_element.attrib:
                UI_element.timeout = float(xml_element.attrib["timeout"])
            if "parent" in xml_element.attrib:
                UI_element.parent_string = xml_element.attrib["parent"]
            if "start_func" in xml_element.attrib:
                UI_element.start_func = self.get_func_by_name(xml_element.attrib["start_func"])
            if "stop_func" in xml_element.attrib:
                UI_element.stop_func = self.get_func_by_name(xml_element.attrib["stop_func"])
            if "identifier" in xml_element.attrib:
                UI_element.identifier_string = xml_element.attrib["identifier"]
                UI_element.identifier = identifier_parser.parse(UI_element.identifier_string, lexer=identifier_lexer)
             
            return UI_element
            
        elif xml_element.tag == "{AXUI}Root_element":
            UI_element = element_module.RootElement()
            
            UI_element.name = xml_element.attrib["name"]
            
            return UI_element
             
        elif xml_element.tag == "{AXUI}UI_element_group":
            UI_element_group = element_module.ElementGroup()

            UI_element_group.name = xml_element.attrib["name"]
            if "timedelay" in xml_element.attrib:
                UI_element_group.timedelay = float(xml_element.attrib["timedelay"])
            if "parent" in xml_element.attrib:
                UI_element_group.parent_string = xml_element.attrib["parent"]
            if "start_func" in xml_element.attrib:
                UI_element_group.start_func = self.get_func_by_name(xml_element.attrib["start_func"])
            if "stop_func" in xml_element.attrib:
                UI_element_group.stop_func = self.get_func_by_name(xml_element.attrib["stop_func"])
            if "identifier" in xml_element.attrib:
                UI_element_group.identifier_string = xml_element.attrib["identifier"]
                UI_element_group.identifier = identifier_parser.parse(UI_element_group.identifier_string, lexer=identifier_lexer)
                
            return UI_element_group

    def _build_UI_element(self, xml_element, parent_UI_element):
        UI_element = self._init_UI_element(xml_element)

        UI_element.parent = parent_UI_element
        parent_UI_element.children[UI_element.name] = UI_element
        
        return UI_element

    def _build_top_level_UI_element(self, xml_element):
        UI_element = self._init_UI_element(xml_element)

        #do nothing for root element
        if isinstance(UI_element, element_module.RootElement):
            return UI_element
            
        #top level element must have parent
        if UI_element.parent_string:
            UI_element.parent = self.get_UI_element_by_name(UI_element.parent_string)
        else:
            raise ValueError("Top level element must have parent attribute, miss parent in element: %s" % UI_element.name)
        
        return UI_element

    def _build_children_UI_elements(self, parent_xml_element, parent_element):  
        for xml_element in list(parent_xml_element):
            UI_element = self._build_UI_element(xml_element, parent_element)            
            self._build_children_UI_elements(xml_element, UI_element)

    def _parse_UI_elements(self, root_element):
        UI_element_root = root_element.find("AXUI:UI_elements", namespaces={"AXUI":"AXUI"})
        if UI_element_root is not None:
            for xml_element in list(UI_element_root):
                UI_element = self._build_top_level_UI_element(xml_element)                
                self.UI_elements[UI_element.name] = UI_element
                self._build_children_UI_elements(xml_element, UI_element)
            
    def parse_all(self):
        '''parse all elements (app_maps, funcs, UI_elements) in the app map
        '''
        element_tree = ET.parse(self.app_map_xml)
        root_element = element_tree.getroot()
        
        self._parse_variable_elements(root_element)
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
        '''get app_map by name list
        name_list should be like "app_map1.app_map2...app_mapX"
        '''
        object_ = self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, AppMap):
            raise ValueError("Expect app map, get %s, please check your name and app map" % type(object_))

    def get_UI_element_by_name(self, name_list):
        '''get element by name
        name_list should be like "app_map1.app_map2...element1.element2...elementX"
        '''
        object_ = self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, element_module.Element):
            raise ValueError("Expect UI element, get %s, please check your name and app map" % type(object_))
        
    def get_func_by_name(self, name_list):
        '''get func by name
        name_list should be like "app_map1.app_map2...app_mapX...func_name"
        '''
        object_ = self._get_object_by_name_list(name_list.split("."))
        if not isinstance(object_, func.Func):
            raise ValueError("Expect func, get %s, please check your name and app map" % type(object_))

    def gui_execute(self, command):
        '''execute gui command
        command like "app_map1.app_map2...element1.element2...operation [parameter1 parameter2 ...]"
        '''
        (object_name_list, parameter_list) = gui_command_parser.parse(command, lexer=gui_command_lexer)
        object_= self._get_object_by_name_list(object_name_list)
        LOGGER().debug("GUI execute %s %s" , object_name_list, parameter_list)
        object_(*parameter_list)
        
    def cli_execute(self, command):
        '''execute cli command
        command like "app parameter1 parameter 2"
        may contain variables
        '''
        args = cli_command_parser.parse(command, lexer=cli_command_lexer)
        #replace variables
        for i, arg in enumerate(args):
            if not re.match("^{.*}$", arg) is None:
                args[i] = self.variables[arg.strip("{").strip("}")]
                
        #some app need to execute in their folder
        app_path = os.path.dirname(args[0])
        if app_path:
            os.chdir(app_path)
                
        LOGGER().debug("CLI execute: %s" , repr(args))
        p = subprocess.Popen(args, shell=True)
        #some app is blocking, do not wait here
        #p.communicate()
        #return p.returncode

    def __getattr__(self, name):
        '''get app_map attribute
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
        
