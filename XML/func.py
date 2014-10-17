

import xml.etree.ElementTree as ET

import AXUI.logger as AXUI_logger
import os
import app_map
import XML_config

LOGGER = AXUI_logger.get_logger()

class FuncMapException(Exception):
    pass

class Step(object):
    def __init__(self, cmd, app_map=None):
        self.cmd = cmd
        self.app_map = app_map
        
    def run(self):
        if self.app_map:
            self.app_map.execute(cmd)
        else:
            os.system(cmd)

class Func(object):
    def __init__(self, xml_func_element, app_maps):
        self.xml_func_element = xml_func_element
        self.app_maps = app_maps
        
        self.name = xml_func_element.attrib["name"]
        self.description = xml_func_element.attrib["description"]
        self.steps = []
        self.parse_steps()
    
    def parse_steps(self):
        for step_element in self.xml_func_element.findall("AXUI_funcs:step", namespaces={"AXUI_funcs":"AXUI_funcs"}):
            step_cmd = step_element.attrib["cmd"]
            try:
                app_map = step_element.attrib["app_map"]
            except KeyError:
                app_map = None
            
            if app_map:
                try:
                    step_app_map = self.app_maps[app_map]
                except:
                    raise FuncMapException("app map:%s used in func: %s not defined"%(app_map, self.name))
            else:
                step_app_map = None
                
            self.steps.append(Step(step_cmd, step_app_map))
            
    def run(self):
        for step in self.steps:
            step.run()
            
def singleton(class_):
    instances = {}
    def getinstance(xml, **kwargs):
        if xml not in instances:
            instances[xml] = class_(xml, **kwargs)
        return instances[xml]
        
    return getinstance
    
@singleton
class FuncMap(object):
    def __init__(self, xml):
        self.func_xml = XML_config.query_app_map_file(xml)
        self.funcs = {}
        self.app_maps = {}
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
        
    def _parse_include_app_map_elements(self, root_element):
        for include_app_map_element in root_element.findall("AXUI_funcs:include_app_map", namespaces={"AXUI_funcs":"AXUI_funcs"}):
            name = include_app_map_element.attrib["name"]
            path = include_app_map_element.attrib["path"]
            self.app_maps[name] = app_map.AppMap(path)
            
    def _parse_func_elements(self, root_element):
        for func_element in root_element.findall("AXUI_funcs:func", namespaces={"AXUI_funcs":"AXUI_funcs"}):
            name = func_element.attrib["name"]
            self.funcs[name] = Func(func_element, self.app_maps)
        
    def parse_elements(self):
        '''
        parse all func elements
        '''
        element_tree = ET.parse(self.func_xml)
        root_element = element_tree.getroot()
        
        self._parse_include_app_map_elements(root_element)
        self._parse_func_elements()
            
    def __getattr__(self, name):
        return self.funcs[name]
        
