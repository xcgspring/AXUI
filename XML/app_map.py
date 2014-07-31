#TODO
#1. Add verification function, including file verify and xml scheme verify
#2. Add exception
#3. Add comments

import xml.etree.ElementTree as ET

import AXUI.logger as logger
import element

class AppMap(object):
    root_element = None
    timeout = 0
    app_map_xml = ""
    all_elements = []

    def __init__(self, xml):
        self.app_map_xml = xml
        self.verification()
        self.build_element_tree()

    def verification(self):
        pass

    def build_element_tree(self):
        tree = ET.parse(self.app_map_xml)
        root = tree.getroot()
        self.root_element = element.Element(root)
        self.root_element.parent = None
        self._get_all_elements(self.root_element)

    def _get_all_elements(self, root_element):
        if len(root_element.children) == 0:
            return
        else:
            for child_element in root_element.children:
                self.all_elements.append(child_element)
                self.get_all_element(child_element)
        
    def get_element_by_ID(self, ID):
        for element in self.all_elements:
            if element.attributes.get("ID") == ID:
                return element
        return None

    def get_element_by_name(self, name):
        for element in self.all_elements:
            if element.attributes.get("name") == name:
                return element
        return None


