
import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
import func
import XML_config

LOGGER = AXUI_logger.get_logger()

class AppMapException(Exception):
    pass

class ElementWrapper(object):
    '''
    wrapper for UI element
    '''
    def __init__(self, name):
        self.name = name
        
        self.children = {}
        self.parent = None
        
        self.start_func = None
        self.start_cmd = ""
        self.identifier = ""
        
        self.UI_element = None
        
        LOGGER.debug("Element wrapper instance for: %s" % self.name)
        
    def bind_UI_element(self):
        '''
        bind this element to according UI element
        '''
        pass
        
    def execute(self, cmd, *params):
        '''
        execute cmd with this element
        '''
        if self.UI_element:
            self.UI_element.execute(cmd)
        else:
            self.bind_UI_element()
            
    def __getattr__(self, name):
        return self.children[name]

class AppMap(object):
    '''
    represent a app map
    '''
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

    def _build_UI_element_wrapper(self, parent_element, parent_element_wrapper):  
        for UI_element in parent_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            name = UI_element.attrib["name"]
            UI_element_wrapper = ElementWrapper(name)
            #get some data for wrapper
            try:
                UI_element_wrapper.identifier = UI_element.attrib["identifier"]
            except KeyError:
                pass
            try:
                UI_element_wrapper.start_cmd = UI_element.attrib["start_cmd"]
            except KeyError:
                pass
            #pair start_func for UI element
            try:
                start_func_string = UI_element.attrib["start_func"]
                UI_element_wrapper.start_func = self.get_func_by_name(start_func_string)
            except KeyError:
                pass
            #build parent-children relationship
            UI_element_wrapper.parent = parent_element_wrapper
            parent_element_wrapper.children[UI_element_wrapper.name] = UI_element_wrapper
            
            self._build_UI_element_wrapper(UI_element, UI_element_wrapper)

    def _parse_UI_element(self, root_element):
        for UI_element in root_element.findall("AXUI:element", namespaces={"AXUI":"AXUI"}):
            name = UI_element.attrib["name"]
            UI_element_wrapper = ElementWrapper(name)
            #get some data for wrapper
            try:
                UI_element_wrapper.identifier = UI_element.attrib["identifier"]
            except KeyError:
                pass
            try:
                UI_element_wrapper.start_cmd = UI_element.attrib["start_cmd"]
            except KeyError:
                pass
            #pair start_func for UI element
            try:
                start_func_string = UI_element.attrib["start_func"]
                UI_element_wrapper.start_func = self.get_func_by_name(start_func_string)
            except KeyError:
                pass
            #build top UI element parent-children relationship
            try:
                parent_string = UI_element.attrib["parent"]
                if not parent_string:
                    LOGGER.debug("Root element have no parent")
                else:
                    UI_element_wrapper.parent = self.get_element_by_name(parent_string)
                    UI_element_wrapper.parent.children[UI_element_wrapper.name] = UI_element_wrapper
            except KeyError:
                raise KeyError("Top level UI Element must have parent element")
                
            self.elements[UI_element_wrapper.name] = UI_element_wrapper
            self._build_UI_element_wrapper(UI_element, UI_element_wrapper)
            
    def parse_elements(self):
        '''
        parse all elements in the app map
        '''
        element_tree = ET.parse(self.app_map_xml)
        root_element = element_tree.getroot()
        
        self._parse_include_app_map_element(root_element)
        self._parse_include_func_element(root_element)
        self._parse_UI_element(root_element)

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
        
