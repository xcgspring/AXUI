# /home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2ec0cd65019e9d98ef3e17d270c6cbd26fe2e263
# Generated 2014-09-04 09:34:57.778890 by PyXB version 1.2.3
# Namespace AXUI_funcs

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:adf4c690-33d3-11e4-a15e-000ffe64bf5a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'AXUI_funcs', create_if_missing=True)
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
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI_funcs}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include'), 'include', '__AXUI_funcs_CTD_ANON_AXUI_funcsinclude', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 14, 4), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {AXUI_funcs}func uses Python identifier func
    __func = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'func'), 'func', '__AXUI_funcs_CTD_ANON_AXUI_funcsfunc', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 21, 4), )

    
    func = property(__func.value, __func.set, None, None)

    _ElementMap.update({
        __include.name() : __include,
        __func.name() : __func
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
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 15, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AXUI_funcs_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 16, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 16, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute path uses Python identifier path
    __path = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'path'), 'path', '__AXUI_funcs_CTD_ANON__path', pyxb.binding.datatypes.string, required=True)
    __path._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 17, 12)
    __path._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 17, 12)
    
    path = property(__path.value, __path.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __path.name() : __path
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 22, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {AXUI_funcs}step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'step'), 'step', '__AXUI_funcs_CTD_ANON_2_AXUI_funcsstep', True, pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 26, 16), )

    
    step = property(__step.value, __step.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AXUI_funcs_CTD_ANON_2_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 23, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 23, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AXUI_funcs_CTD_ANON_2_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 24, 12)
    __description._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 24, 12)
    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __step.name() : __step
    })
    _AttributeMap.update({
        __name.name() : __name,
        __description.name() : __description
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 27, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute cmd uses Python identifier cmd
    __cmd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cmd'), 'cmd', '__AXUI_funcs_CTD_ANON_3_cmd', pyxb.binding.datatypes.string, required=True)
    __cmd._DeclarationLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 28, 24)
    __cmd._UseLocation = pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 28, 24)
    
    cmd = property(__cmd.value, __cmd.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __cmd.name() : __cmd
    })



funcs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'funcs'), CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', funcs.name().localName(), funcs)

include = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', include.name().localName(), include)

func = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'func'), CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 21, 4))
Namespace.addCategoryObject('elementBinding', func.name().localName(), func)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 14, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'func'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 21, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'func')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 9, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'step'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 26, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'step')), pyxb.utils.utility.Location('/home/cxuanx/gitHub/AXUI/XML/schemas/AXUI_funcs.xsd', 26, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()

