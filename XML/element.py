#TODO
#1. Add UI bind function
#2. Add comments

import AXUI.logger as logger

class Element(object):
    attributes = {
        'ID':'',
        'name':'',
        'search_condition':'',
        'start_operation':'',
        'timeout':'',
        'if_validate':True,
        'reference_picture':''
    }

    parent = None
    children = []
    associate_UI_element = None

    def __init__(self, xml_element):
        for attrib in self.attributes.items():
            attrib_key = attrib[0]
            attrib[attrib_key] = xml_element.attrib.get(attrib_key)

        for child_element in xml_element.findall("."):
            child = Element(child_element)
            child.parent = self
            self.children.append(child)

    def bind_UI_element(self):
        pass

