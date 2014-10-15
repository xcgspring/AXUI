

import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
import XML_config

LOGGER = AXUI_logger.get_logger()

class Func(object):
    def __init__(self, xml_func_element):
        self.xml_func_element = xml_func_element
        self.name = xml_func_element.attrib["name"]
        self.description = xml_func_element.attrib["description"]
        self.steps = []
        self.parse_steps()
    
    def parse_steps(self):
        for step_element in self.xml_func_element.findall("AXUI_funcs:step", namespaces={"AXUI_funcs":"AXUI_funcs"}):
            self.steps.append(step_element.attrib["cmd"])

class FuncMap(object):
    def __init__(self, xml):
        self.func_xml = XML_config.query_app_map_file(xml)
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
            self.logger.info("pyxb not install, skip app map verification")
            return
            
        from validate import check_app_map
        check_app_map(XML_config.query_schema_file("AXUI_funcs.xsd"), self.func_xml)
        
    def parse_elements(self):
        '''
        parse all func elements
        '''
        element_tree = ET.parse(self.func_xml)
        root_element = element_tree.getroot()
        
        for func_element in root_element.findall("AXUI_funcs:func", namespaces={"AXUI_funcs":"AXUI_funcs"}):
            name = func_element.attrib["name"]
            self.funcs[name] = Func(func_element)
            
    def __getattr__(self, name):
        return self.funcs[name]
        
