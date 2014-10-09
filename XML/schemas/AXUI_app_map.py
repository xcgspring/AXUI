# /home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a2298868df588524980a3d50949db96b28be61f4
# Generated 2014-10-09 17:06:42.847192 by PyXB version 1.2.3
# Namespace AXUI

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:964a0ca4-4f93-11e4-a20d-000ffe64bf5a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'AXUI', create_if_missing=True)
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
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
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
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}include_app_map uses Python identifier include_app_map
    __include_app_map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include_app_map'), 'include_app_map', '__AXUI_CTD_ANON_AXUIinclude_app_map', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 15, 4), )

    
    include_app_map = property(__include_app_map.value, __include_app_map.set, None, None)

    
    # Element {AXUI}include_func uses Python identifier include_func
    __include_func = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include_func'), 'include_func', '__AXUI_CTD_ANON_AXUIinclude_func', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 22, 4), )

    
    include_func = property(__include_func.value, __include_func.set, None, None)

    
    # Element {AXUI}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'element'), 'element', '__AXUI_CTD_ANON_AXUIelement', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 29, 4), )

    
    element = property(__element.value, __element.set, None, None)

    _ElementMap.update({
        __include_app_map.name() : __include_app_map,
        __include_func.name() : __include_func,
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 16, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AXUI_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 17, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 17, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__AXUI_CTD_ANON__path', pyxb.binding.datatypes.string, required=True)
    __path._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 18, 12)
    __path._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 18, 12)
    
    path = property(__path.value, __path.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __path.name() : __path
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 23, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AXUI_CTD_ANON_2_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 24, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 24, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__AXUI_CTD_ANON_2_path', pyxb.binding.datatypes.string, required=True)
    __path._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 25, 12)
    __path._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 25, 12)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 30, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI}element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'element'), 'element', '__AXUI_CTD_ANON_3_AXUIelement', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 29, 4), )

    
    element = property(__element.value, __element.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AXUI_CTD_ANON_3_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 31, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 31, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parent'), 'parent', '__AXUI_CTD_ANON_3_parent', pyxb.binding.datatypes.string)
    __parent._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 32, 12)
    __parent._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 32, 12)
    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'identifier'), 'identifier', '__AXUI_CTD_ANON_3_identifier', pyxb.binding.datatypes.string)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 33, 12)
    __identifier._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 33, 12)
    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Attribute start_cmd uses Python identifier start_cmd
    __start_cmd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'start_cmd'), 'start_cmd', '__AXUI_CTD_ANON_3_start_cmd', pyxb.binding.datatypes.string)
    __start_cmd._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 34, 12)
    __start_cmd._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 34, 12)
    
    start_cmd = property(__start_cmd.value, __start_cmd.set, None, None)

    
    # Attribute start_func uses Python identifier start_func
    __start_func = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'start_func'), 'start_func', '__AXUI_CTD_ANON_3_start_func', pyxb.binding.datatypes.string)
    __start_func._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 35, 12)
    __start_func._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 35, 12)
    
    start_func = property(__start_func.value, __start_func.set, None, None)

    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        __name.name() : __name,
        __parent.name() : __parent,
        __identifier.name() : __identifier,
        __start_cmd.name() : __start_cmd,
        __start_func.name() : __start_func
    })



elements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'elements'), CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', elements.name().localName(), elements)

include_app_map = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include_app_map'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', include_app_map.name().localName(), include_app_map)

include_func = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include_func'), CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', include_func.name().localName(), include_func)

element = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'element'), CTD_ANON_3, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 29, 4))
Namespace.addCategoryObject('elementBinding', element.name().localName(), element)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include_app_map'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 15, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include_func'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 22, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'element'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 29, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 7, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include_app_map')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include_func')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 9, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'element')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 10, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'element'), CTD_ANON_3, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 29, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'element')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_app_map.xsd', 37, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_()

