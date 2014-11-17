# C:\Users\cxuanx\Desktop\tmp\AXUI\XML\schemas\AXUI_app_map.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a2298868df588524980a3d50949db96b28be61f4
# Generated 2014-11-17 10:17:31.565000 by PyXB version 1.2.4 using Python 2.7.0.final.0
# Namespace AXUI

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e2af60f0-6dff-11e4-8e6f-001b211bc956')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('AXUI', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}includes uses Python identifier includes
    __includes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'includes'), 'includes', '__AXUI_CTD_ANON_AXUIincludes', False, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 15, 4), )

    
    includes = property(__includes.value, __includes.set, None, None)

    
    # Element {AXUI}funcs uses Python identifier funcs
    __funcs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'funcs'), 'funcs', '__AXUI_CTD_ANON_AXUIfuncs', False, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 30, 4), )

    
    funcs = property(__funcs.value, __funcs.set, None, None)

    
    # Element {AXUI}UI_elements uses Python identifier UI_elements
    __UI_elements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UI_elements'), 'UI_elements', '__AXUI_CTD_ANON_AXUIUI_elements', False, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 54, 4), )

    
    UI_elements = property(__UI_elements.value, __UI_elements.set, None, None)

    _ElementMap.update({
        __includes.name() : __includes,
        __funcs.name() : __funcs,
        __UI_elements.name() : __UI_elements
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 16, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__AXUI_CTD_ANON__AXUIinclude', True, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 23, 4), )

    
    include = property(__include.value, __include.set, None, None)

    _ElementMap.update({
        __include.name() : __include
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 24, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AXUI_CTD_ANON_2_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 25, 12)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 25, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__AXUI_CTD_ANON_2_path', pyxb.binding.datatypes.string, required=True)
    __path._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 26, 12)
    __path._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 26, 12)
    
    path = property(__path.value, __path.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __path.name() : __path
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 31, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}func uses Python identifier func
    __func = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'func'), 'func', '__AXUI_CTD_ANON_3_AXUIfunc', True, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 38, 4), )

    
    func = property(__func.value, __func.set, None, None)

    _ElementMap.update({
        __func.name() : __func
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 39, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'step'), 'step', '__AXUI_CTD_ANON_4_AXUIstep', True, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 43, 16), )

    
    step = property(__step.value, __step.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AXUI_CTD_ANON_4_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 40, 12)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 40, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AXUI_CTD_ANON_4_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 41, 12)
    __description._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 41, 12)
    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __step.name() : __step
    })
    _AttributeMap.update({
        __name.name() : __name,
        __description.name() : __description
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 44, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AXUI_CTD_ANON_5_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 45, 24)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 45, 24)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute cmd uses Python identifier cmd
    __cmd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cmd'), 'cmd', '__AXUI_CTD_ANON_5_cmd', pyxb.binding.datatypes.string, required=True)
    __cmd._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 46, 24)
    __cmd._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 46, 24)
    
    cmd = property(__cmd.value, __cmd.set, None, None)

    
    # Attribute app_map uses Python identifier app_map
    __app_map = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'app_map'), 'app_map', '__AXUI_CTD_ANON_5_app_map', pyxb.binding.datatypes.string)
    __app_map._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 47, 24)
    __app_map._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 47, 24)
    
    app_map = property(__app_map.value, __app_map.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __cmd.name() : __cmd,
        __app_map.name() : __app_map
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 55, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}UI_element uses Python identifier UI_element
    __UI_element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UI_element'), 'UI_element', '__AXUI_CTD_ANON_6_AXUIUI_element', True, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 62, 4), )

    
    UI_element = property(__UI_element.value, __UI_element.set, None, None)

    _ElementMap.update({
        __UI_element.name() : __UI_element
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 63, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}UI_element uses Python identifier UI_element
    __UI_element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UI_element'), 'UI_element', '__AXUI_CTD_ANON_7_AXUIUI_element', True, pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 62, 4), )

    
    UI_element = property(__UI_element.value, __UI_element.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AXUI_CTD_ANON_7_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 64, 12)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 64, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__AXUI_CTD_ANON_7_parent', pyxb.binding.datatypes.string)
    __parent._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 65, 12)
    __parent._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 65, 12)
    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AXUI_CTD_ANON_7_identifier', pyxb.binding.datatypes.string)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 66, 12)
    __identifier._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 66, 12)
    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Attribute start_func uses Python identifier start_func
    __start_func = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start_func'), 'start_func', '__AXUI_CTD_ANON_7_start_func', pyxb.binding.datatypes.string)
    __start_func._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 67, 12)
    __start_func._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 67, 12)
    
    start_func = property(__start_func.value, __start_func.set, None, None)

    
    # Attribute stop_func uses Python identifier stop_func
    __stop_func = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stop_func'), 'stop_func', '__AXUI_CTD_ANON_7_stop_func', pyxb.binding.datatypes.string)
    __stop_func._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 68, 12)
    __stop_func._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 68, 12)
    
    stop_func = property(__stop_func.value, __stop_func.set, None, None)

    
    # Attribute timeout uses Python identifier timeout
    __timeout = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'timeout'), 'timeout', '__AXUI_CTD_ANON_7_timeout', pyxb.binding.datatypes.decimal)
    __timeout._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 69, 12)
    __timeout._UseLocation = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 69, 12)
    
    timeout = property(__timeout.value, __timeout.set, None, None)

    _ElementMap.update({
        __UI_element.name() : __UI_element
    })
    _AttributeMap.update({
        __name.name() : __name,
        __parent.name() : __parent,
        __identifier.name() : __identifier,
        __start_func.name() : __start_func,
        __stop_func.name() : __stop_func,
        __timeout.name() : __timeout
    })



app_map = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'app_map'), CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', app_map.name().localName(), app_map)

includes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includes'), CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', includes.name().localName(), includes)

include = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), CTD_ANON_2, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', include.name().localName(), include)

funcs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'funcs'), CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 30, 4))
Namespace.addCategoryObject('elementBinding', funcs.name().localName(), funcs)

func = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'func'), CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 38, 4))
Namespace.addCategoryObject('elementBinding', func.name().localName(), func)

UI_elements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UI_elements'), CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 54, 4))
Namespace.addCategoryObject('elementBinding', UI_elements.name().localName(), UI_elements)

UI_element = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UI_element'), CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 62, 4))
Namespace.addCategoryObject('elementBinding', UI_element.name().localName(), UI_element)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'includes'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 15, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'funcs'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 30, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UI_elements'), CTD_ANON_6, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 54, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 8, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'includes')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 9, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'funcs')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 9, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 10, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UI_elements')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 10, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 8, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 9, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 10, 16))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    final_update = set()
    symbol = pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 7, 12)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 23, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 18, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'func'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 38, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'func')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 33, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'step'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 43, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'step')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 43, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UI_element'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 62, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 56, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UI_element')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 57, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UI_element'), CTD_ANON_7, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 62, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 70, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UI_element')), pyxb.utils.utility.Location('C:\\Users\\cxuanx\\Desktop\\tmp\\AXUI\\XML\\schemas\\AXUI_app_map.xsd', 71, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()

