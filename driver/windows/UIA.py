'''
Use comtypes to generate python wrapper for windows native UIA API

Comtypes: 
    https://github.com/enthought/comtypes
Windows native UIA API: 
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee671216(v=vs.85).aspx
'''

from comtypes.client import GetModule, CreateObject
from AXUI.logger import logger
from ctypes import POINTER

LOGGER = logger.get_logger()

class UIAException(Exception):
    pass

UIA_type_lib_IID = '{944DE083-8FB8-45CF-BCB7-C477ACB2F897}'
#generate UIA python wrapper
UIA_wrapper = GetModule((UIA_type_lib_IID, 1, 0))
#create object of IUIAutomation
IUIAutomation_object = CreateObject(UIA_wrapper.CUIAutomation, None, None, UIA_wrapper.IUIAutomation)

#UIA Automation Element Property Identifiers
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx
#You can check element property using inspect.exe
#http://msdn.microsoft.com/en-us/library/windows/desktop/dd318521(v=vs.85).aspx
UIA_property_identifers = (
    "AcceleratorKey",
    "AccessKey",
    "AriaProperties",
    "AriaRole",
    "AutomationId",
    "BoundingRectangle",
    "ClassName",
    "ClickablePoint",
    "ControllerFor",
    "ControlType",
    "Culture",
    "DescribedBy",
    "FlowsFrom",
    "FlowsTo",
    "FrameworkId",
    "HasKeyboardFocus",
    "HelpText",
    "IsContentElement",
    "IsControlElement",
    "IsDataValidForForm",
    "IsEnabled",
    "IsKeyboardFocusable",
    "IsOffscreen",
    "IsPassword",
    "IsPeripheral",
    "IsRequiredForForm",
    "ItemStatus",
    "ItemType",
    "LabeledBy",
    "LiveSetting",
    "LocalizedControlType",
    "Name",
    "NativeWindowHandle",
    "OptimizeForVisualContent",
    "Orientation",
    "ProcessId",
    "ProviderDescription",
    "RuntimeId",
    )
    
#UIA Control Pattern Identifiers
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee671195(v=vs.85).aspx
UIA_Pattern_identifers = (
    "AnnotationPattern",
    "DockPattern",
    "DragPattern",
    "DropPattern",
    "ExpandCollapsePattern",
    "GridItemPattern",
    "GridPattern",
    "InvokePattern",
    "ItemContainerPattern",
    "LegacyIAccessiblePattern",
    "MultipleViewPattern",
    "ObjectModelPattern",
    "RangeValuePattern",
    "ScrollItemPattern",
    "ScrollPattern",
    "SelectionItemPattern",
    "SelectionPattern",
    "SpreadsheetPattern",
    "SpreadsheetItemPattern",
    "StylesPattern",
    "SynchronizedInputPattern",
    "TableItemPattern",
    "TablePattern",
    "TextChildPattern",
    "TextEditPattern",
    "TextPattern",
    "TextPattern2",
    "TogglePattern",
    "TransformPattern",
    "TransformPattern2",
    "ValuePattern",
    "VirtualizedItemPattern",
    "WindowPattern",
    )
    
def get_property_by_id(UIAElement, property_identifier):
    '''
    get property by identifier
    '''
    try:
        UIA_property_identifier = getattr(UIA_wrapper, "UIA_"+property_identifier+"PropertyId")
    except AttributeError:
        LOGGER.error("Not support property identifier: %s" % property_identifier)
        LOGGER.warn("Sample property identifiers:\n"+repr(UIA_property_identifers))
        raise UIAException("Not support property identifier: %s" % property_identifier)
        
    return repr(UIAElement.GetCurrentPropertyValue(UIA_property_identifier))
    
def get_pattern_by_id(UIAElement, pattern_identifier):
    '''
    get pattern by identifier
    '''
    try:
        UIA_pattern_identifier = getattr(UIA_wrapper, "UIA_"+pattern_identifier+"Id")
        UIA_pattern_interface = getattr(UIA_wrapper, "IUIAutomation"+pattern_identifier)
    except AttributeError:
        LOGGER.error("Not support pattern identifier: %s" % pattern_identifier)
        LOGGER.warn("Sample pattern identifiers:\n"+repr(UIA_pattern_identifers))
        raise UIAException("Not support pattern identifier: %s" % pattern_identifier)
    
    return POINTER(UIA_pattern_interface)(UIAElement.GetCurrentPatternAs(UIA_pattern_identifier, UIA_pattern_interface._iid_))
    
