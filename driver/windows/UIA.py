'''
Use comtypes to generate python wrapper for windows native UIA API
This module should keep update with latest UIA version

Comtypes: 
    https://github.com/enthought/comtypes
    https://pythonhosted.org/comtypes/
Windows native UIA API: 
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee671216(v=vs.85).aspx
'''

from comtypes.client import GetModule, CreateObject
from AXUI.logger import logger
from ctypes import *

LOGGER = logger.get_logger()

class UIAException(Exception):
    pass

UIA_type_lib_IID = '{944DE083-8FB8-45CF-BCB7-C477ACB2F897}'
#generate UIA python wrapper
UIA_wrapper = GetModule((UIA_type_lib_IID, 1, 0))
#create object of IUIAutomation
IUIAutomation_object = CreateObject(UIA_wrapper.CUIAutomation, None, None, UIA_wrapper.IUIAutomation)

##############################
#UI Automation Enumerations
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee671210(v=vs.85).aspx
##############################
UIA_enum = {
"ActiveEnd"     : {
    "ActiveEnd_None": None
           "ActiveEnd_Start": None
           "ActiveEnd_End": None}
"AnimationStyle": ("AnimationStyle_LasVegasLights",
                  "")

}




















###############################
#UI Automation Constants
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee671207(v=vs.85).aspx

#You can check element property and pattern using inspect.exe
#http://msdn.microsoft.com/en-us/library/windows/desktop/dd318521(v=vs.85).aspx
###############################

#Automation Element Property Identifiers
UIA_automation_element_property_identifers = (
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
    
#Control Pattern Property Identifiers
UIA_control_pattern_property_identifiers = (
    "AnnotationAnnotationTypeId",
    "AnnotationAnnotationTypeName",
    "AnnotationAuthor",
    "AnnotationDateTime",
    "AnnotationTarget",
    "DockDockPosition",
    "DragDropEffect",
    "DragDropEffects",
    "DragIsGrabbed",
    "DragGrabbedItems",
    "DropTargetDropTargetEffect",
    "DropTargetDropTargetEffects",
    "ExpandCollapseExpandCollapseState",
    "GridColumnCount",
    "GridItemColumn",
    "GridItemColumnSpan",
    "GridItemContainingGrid",
    "GridItemRow",
    "GridItemRowSpan",
    "GridRowCount",
    "LegacyIAccessibleChildId",
    "LegacyIAccessibleDefaultAction",
    "LegacyIAccessibleDescription",
    "LegacyIAccessibleHelp",
    "LegacyIAccessibleKeyboardShortcut",
    "LegacyIAccessibleName",
    "LegacyIAccessibleRole",
    "LegacyIAccessibleSelection",
    "LegacyIAccessibleState",
    "LegacyIAccessibleValue",
    "MultipleViewCurrentView",
    "MultipleViewSupportedViews",
    "RangeValueIsReadOnly",
    "RangeValueLargeChange",
    "RangeValueMaximum",
    "RangeValueMinimum",
    "RangeValueSmallChange",
    "RangeValueValue",
    "ScrollHorizontallyScrollable",
    "ScrollHorizontalScrollPercent",
    "ScrollHorizontalViewSize",
    "ScrollVerticallyScrollable",
    "ScrollVerticalScrollPercent",
    "ScrollVerticalViewSize",
    "SelectionCanSelectMultiple",
    "SelectionIsSelectionRequired",
    "SelectionSelection",
    "SelectionItemIsSelected",
    "SelectionItemSelectionContainer",
    "SpreadsheetItemFormula",
    "SpreadsheetItemAnnotationObjects",
    "SpreadsheetItemAnnotationTypes",
    "StylesExtendedProperties",
    "StylesFillColor",
    "StylesFillPatternColor",
    "StylesFillPatternStyle",
    "StylesShape",
    "StylesStyleId",
    "StylesStyleName",
    "TableColumnHeaders",
    "TableItemColumnHeaderItems",
    "TableRowHeaders",
    "TableRowOrColumnMajor",
    "TableItemRowHeaderItems",
    "ToggleToggleState",
    "TransformCanMove",
    "TransformCanResize",
    "TransformCanRotate",
    "Transform2CanZoom",
    "Transform2ZoomLevel",
    "Transform2ZoomMaximum",
    "Transform2ZoomMinimum",
    "ValueIsReadOnly",
    "ValueValue",
    "WindowCanMaximize",
    "WindowCanMinimize",
    "WindowIsModal",
    "WindowIsTopmost",
    "WindowWindowInteractionState",
    "WindowWindowVisualState",
    )
    
#Pattern interfaces description
UIA_control_pattern_interfaces = {
"AnnotationPattern"         : [
    ('property', 'CurrentAnnotationTypeId',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentAnnotationTypeName',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentAuthor',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentDateTime',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentTarget',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
    ('property', 'CachedAnnotationTypeId',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedAnnotationTypeName',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedAuthor',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedDateTime',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedTarget',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
],
"DockPattern"               : [
    ('method', 'SetDockPosition',
              ( 'in', DockPosition, 'dockPos' )),
    ('property', 'CurrentDockPosition',
              ( 'out', 'POINTER(DockPosition)', 'retVal' )),
    ('property', 'CachedDockPosition',
              ( 'out', 'POINTER(DockPosition)', 'retVal' )),
],
"DragPattern"               : [
    ('property', 'CurrentIsGrabbed',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedIsGrabbed',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentDropEffect',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedDropEffect',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentDropEffects',
              ( 'out', 'POINTER(_midlSAFEARRAY(BSTR))', 'retVal' )),
    ('property', 'CachedDropEffects',
              ( 'out', 'POINTER(_midlSAFEARRAY(BSTR))', 'retVal' )),
    ('method', 'GetCurrentGrabbedItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCachedGrabbedItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
],
"DropTargetPattern"         : [
    ('property', 'CurrentDropTargetEffect',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedDropTargetEffect',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentDropTargetEffects',
              ( 'out', 'POINTER(_midlSAFEARRAY(BSTR))', 'retVal' )),
    ('property', 'CachedDropTargetEffects',
              ( 'out', 'POINTER(_midlSAFEARRAY(BSTR))', 'retVal' )),
],
"ExpandCollapsePattern"     : [
    ('method', 'Expand'),
    ('method', 'Collapse'),
    ('property', 'CurrentExpandCollapseState',
              ( 'out', 'POINTER(ExpandCollapseState)', 'retVal' )),
    ('property', 'CachedExpandCollapseState',
              ( 'out', 'POINTER(ExpandCollapseState)', 'retVal' )),
],
"GridItemPattern"           : [
    ('property', 'CurrentContainingGrid',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
    ('property', 'CurrentRow',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentColumn',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentRowSpan',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentColumnSpan',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedContainingGrid',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
    ('property', 'CachedRow',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedColumn',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedRowSpan',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedColumnSpan',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
],
"GridPattern"               : [
    ('method', 'GetItem',
              ( 'in', c_int, 'row' ),
              ( 'in', c_int, 'column' ),
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'element' )),
    ('property', 'CurrentRowCount',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentColumnCount',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedRowCount',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedColumnCount',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
],
"InvokePattern"             : [
    ('method', 'Invoke'),
],
"ItemContainerPattern"      : [
    ('method', 'FindItemByProperty',
              ( 'in', POINTER(IUIAutomationElement), 'pStartAfter' ),
              ( 'in', c_int, 'propertyId' ),
              ( 'in', VARIANT, 'value' ),
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'pFound' )),
],
"LegacyIAccessiblePattern"  : [
    ('method', 'Select',
              ( 'method', c_int, 'flagsSelect' )),
    ('method', 'DoDefaultAction'),
    ('method', 'SetValue',
              ( 'method', WSTRING, 'szValue' )),
    ('property', 'CurrentChildId',
              ( 'out', 'POINTER(c_int)', 'pRetVal' )),
    ('property', 'CurrentName',
              ( 'out', 'POINTER(BSTR)', 'pszName' )),
    ('property', 'CurrentValue',
              ( 'out', 'POINTER(BSTR)', 'pszValue' )),
    ('property', 'CurrentDescription',
              ( 'out', 'POINTER(BSTR)', 'pszDescription' )),
    ('property', 'CurrentRole',
              ( 'out', 'POINTER(c_ulong)', 'pdwRole' )),
    ('property', 'CurrentState',
              ( 'out', 'POINTER(c_ulong)', 'pdwState' )),
    ('property', 'CurrentHelp',
              ( 'out', 'POINTER(BSTR)', 'pszHelp' )),
    ('property', 'CurrentKeyboardShortcut',
              ( 'out', 'POINTER(BSTR)', 'pszKeyboardShortcut' )),
    ('method', 'GetCurrentSelection',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'pvarSelectedChildren' )),
    ('property', 'CurrentDefaultAction',
              ( 'out', 'POINTER(BSTR)', 'pszDefaultAction' )),
    ('property', 'CachedChildId',
              ( 'out', 'POINTER(c_int)', 'pRetVal' )),
    ('property', 'CachedName',
              ( 'out', 'POINTER(BSTR)', 'pszName' )),
    ('property', 'CachedValue',
              ( 'out', 'POINTER(BSTR)', 'pszValue' )),
    ('property', 'CachedDescription',
              ( 'out', 'POINTER(BSTR)', 'pszDescription' )),
    ('property', 'CachedRole',
              ( 'out', 'POINTER(c_ulong)', 'pdwRole' )),
    ('property', 'CachedState',
              ( 'out', 'POINTER(c_ulong)', 'pdwState' )),
    ('property', 'CachedHelp',
              ( 'out', 'POINTER(BSTR)', 'pszHelp' )),
    ('property', 'CachedKeyboardShortcut',
              ( 'out', 'POINTER(BSTR)', 'pszKeyboardShortcut' )),
    ('method', 'GetCachedSelection',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'pvarSelectedChildren' )),
    ('property', 'CachedDefaultAction',
              ( 'out', 'POINTER(BSTR)', 'pszDefaultAction' )),
    ('method', 'GetIAccessible',
              ( 'out', 'POINTER(POINTER(IAccessible))', 'ppAccessible' )),
],
"MultipleViewPattern"       : [
    ('method', 'GetViewName',
              ( 'in', c_int, 'view' ),
              ( 'out', POINTER(BSTR), 'name' )),
    ('method', 'SetCurrentView',
              ( 'in', c_int, 'view' )),
    ('property', 'CurrentCurrentView',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('method', 'GetCurrentSupportedViews',
              ( 'out', POINTER(_midlSAFEARRAY(c_int)), 'retVal' )),
    ('property', 'CachedCurrentView',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('method', 'GetCachedSupportedViews',
              ( 'out', POINTER(_midlSAFEARRAY(c_int)), 'retVal' )),
],
"ObjectModelPattern"        : [
    ('method', 'GetUnderlyingObjectModel',
              ( 'out', POINTER(POINTER(IUnknown)), 'retVal' )),
],
"RangeValuePattern"         : [
    ('method', 'SetValue',
              ( 'in', c_double, 'val' )),
    ('property', 'CurrentValue',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentIsReadOnly',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentLargeChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentSmallChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedValue',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedIsReadOnly',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedLargeChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedSmallChange',
              ( 'out', POINTER(c_double), 'retVal' )),
],
"ScrollItemPattern"         : [
    ('method', 'ScrollIntoView'),
],
"ScrollPattern"             : [
    ('method', 'Scroll',
              ( 'in', ScrollAmount, 'horizontalAmount' ),
              ( 'in', ScrollAmount, 'verticalAmount' )),
    ('method', 'SetScrollPercent',
              ( 'in', c_double, 'horizontalPercent' ),
              ( 'in', c_double, 'verticalPercent' )),
    ('property', 'CurrentHorizontalScrollPercent',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentVerticalScrollPercent',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentHorizontalViewSize',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentVerticalViewSize',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentHorizontallyScrollable',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentVerticallyScrollable',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedHorizontalScrollPercent',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedVerticalScrollPercent',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedHorizontalViewSize',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedVerticalViewSize',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedHorizontallyScrollable',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedVerticallyScrollable',
              ( 'out', POINTER(c_int), 'retVal' )),
],
"SelectionItemPattern"      : [
    ('method', 'Select'),
    ('method', 'AddToSelection'),
    ('method', 'RemoveFromSelection'),
    ('property', 'CurrentIsSelected',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentSelectionContainer',
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'retVal' )),
    ('property', 'CachedIsSelected',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedSelectionContainer',
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'retVal' )),
],
"SelectionPattern"          : [
    ('method', 'GetCurrentSelection',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('property', 'CurrentCanSelectMultiple',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentIsSelectionRequired',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('method', 'GetCachedSelection',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('property', 'CachedCanSelectMultiple',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedIsSelectionRequired',
              ( 'out', POINTER(c_int), 'retVal' )),
],
"SpreadsheetPattern"        : [
    ('method', 'GetItemByName',
              ( 'in', BSTR, 'name' ),
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'element' )),
],
"SpreadsheetItemPattern"    : [
    ('property', 'CurrentFormula',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('method', 'GetCurrentAnnotationObjects',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCurrentAnnotationTypes',
              ( 'out', POINTER(_midlSAFEARRAY(c_int)), 'retVal' )),
    ('property', 'CachedFormula',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('method', 'GetCachedAnnotationObjects',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCachedAnnotationTypes',
              ( 'out', POINTER(_midlSAFEARRAY(c_int)), 'retVal' )),
],
"StylesPattern"             : [
    ('property', 'CurrentStyleId',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentStyleName',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CurrentFillColor',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentFillPatternStyle',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CurrentShape',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CurrentFillPatternColor',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentExtendedProperties',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('method', 'GetCurrentExtendedPropertiesAsArray',
              ( 'out', POINTER(POINTER(ExtendedProperty)), 'propertyArray' ),
              ( 'out', POINTER(c_int), 'propertyCount' )),
    ('property', 'CachedStyleId',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedStyleName',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CachedFillColor',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedFillPatternStyle',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CachedShape',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('property', 'CachedFillPatternColor',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedExtendedProperties',
              ( 'out', POINTER(BSTR), 'retVal' )),
    ('method', 'GetCachedExtendedPropertiesAsArray',
              ( 'out', POINTER(POINTER(ExtendedProperty)), 'propertyArray' ),
              ( 'out', POINTER(c_int), 'propertyCount' )),
],
"SynchronizedInputPattern"  : [
    ('method', 'StartListening',
              ( 'in', SynchronizedInputType, 'inputType' )),
    ('method', 'Cancel'),
],
"TableItemPattern"          : [
    ('method', 'GetCurrentRowHeaderItems',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCurrentColumnHeaderItems',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCachedRowHeaderItems',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCachedColumnHeaderItems',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
],
"TablePattern"              : [
    ('method', 'GetCurrentRowHeaders',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCurrentColumnHeaders',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('property', 'CurrentRowOrColumnMajor',
              ( 'out', POINTER(RowOrColumnMajor), 'retVal' )),
    ('method', 'GetCachedRowHeaders',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('method', 'GetCachedColumnHeaders',
              ( 'out', POINTER(POINTER(IUIAutomationElementArray)), 'retVal' )),
    ('property', 'CachedRowOrColumnMajor',
              ( 'out', POINTER(RowOrColumnMajor), 'retVal' )),
],
"TextChildPattern"          : [
    ('property', 'TextContainer',
              ( 'out', POINTER(POINTER(IUIAutomationElement)), 'container' )),
    ('property', 'TextRange',
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
],
"TextEditPattern"           : None,
"TextPattern"               : [
    ('method', 'RangeFromPoint',
              ( 'in', tagPOINT, 'pt' ),
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
    ('method', 'RangeFromChild',
              ( 'in', POINTER(IUIAutomationElement), 'child' ),
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
    ('method', 'GetSelection',
              ( 'out', POINTER(POINTER(IUIAutomationTextRangeArray)), 'ranges' )),
    ('method', 'GetVisibleRanges',
              ( 'out', POINTER(POINTER(IUIAutomationTextRangeArray)), 'ranges' )),
    ('property', 'DocumentRange',
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
    ('property', 'SupportedTextSelection',
              ( 'out', POINTER(SupportedTextSelection), 'SupportedTextSelection' )),
],
"TextPattern2"              : [
    ('method', 'RangeFromAnnotation',
              ( 'in', POINTER(IUIAutomationElement), 'annotation' ),
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
    ('method', 'GetCaretRange',
              ( 'out', POINTER(c_int), 'isActive' ),
              ( 'out', POINTER(POINTER(IUIAutomationTextRange)), 'range' )),
],
"TogglePattern"             : [
    ('method', 'Toggle'),
    ('property', 'CurrentToggleState',
              ( 'out', POINTER(ToggleState), 'retVal' )),
    ('property', 'CachedToggleState',
              ( 'out', POINTER(ToggleState), 'retVal' )),
],
"TransformPattern"          : [
    ('method', 'Move',
              ( 'in', c_double, 'x' ),
              ( 'in', c_double, 'y' )),
    ('method', 'Resize',
              ( 'in', c_double, 'width' ),
              ( 'in', c_double, 'height' )),
    ('method', 'Rotate',
              ( 'in', c_double, 'degrees' )),
    ('property', 'CurrentCanMove',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentCanResize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentCanRotate',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedCanMove',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedCanResize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedCanRotate',
              ( 'out', POINTER(c_int), 'retVal' )),
],
"TransformPattern2"         : [
    ('method', 'Zoom',
              ( 'in', c_double, 'Zoom' )),
    ('method', 'ZoomByUnit',
              ( 'in', ZoomUnit, 'ZoomUnit' )),
    ('property', 'CurrentCanZoom',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedCanZoom',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentZoomLevel',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedZoomLevel',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentZoomMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedZoomMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentZoomMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedZoomMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
],
"ValuePattern"              : [
    ('method', 'SetValue',
              ( 'in', c_double, 'val' )),
    ('property', 'CurrentValue',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentIsReadOnly',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentLargeChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CurrentSmallChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedValue',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedIsReadOnly',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedMaximum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedMinimum',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedLargeChange',
              ( 'out', POINTER(c_double), 'retVal' )),
    ('property', 'CachedSmallChange',
              ( 'out', POINTER(c_double), 'retVal' )),
],
"VirtualizedItemPattern"    : [
    ('method', 'Realize'),
],
"WindowPattern"             : [
    ('method', 'Close'),
    ('method', 'WaitForInputIdle',
              ( 'in', c_int, 'milliseconds' ),
              ( 'out', POINTER(c_int), 'success' )),
    ('method', 'SetWindowVisualState',
              ( 'in', WindowVisualState, 'state' )),
    ('property', 'CurrentCanMaximize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentCanMinimize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentIsModal',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentIsTopmost',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CurrentWindowVisualState',
              ( 'out', POINTER(WindowVisualState), 'retVal' )),
    ('property', 'CurrentWindowInteractionState',
              ( 'out', POINTER(WindowInteractionState), 'retVal' )),
    ('property', 'CachedCanMaximize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedCanMinimize',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedIsModal',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedIsTopmost',
              ( 'out', POINTER(c_int), 'retVal' )),
    ('property', 'CachedWindowVisualState',
              ( 'out', POINTER(WindowVisualState), 'retVal' )),
    ('property', 'CachedWindowInteractionState',
              ( 'out', POINTER(WindowInteractionState), 'retVal' )),
],
}

#Control Pattern Identifiers
UIA_control_pattern_identifers = UIA_control_pattern_interfaces.keys()

#Control Pattern Availability Property Identifiers
UIA_control_pattern_availability_property_identifiers = 
[ "Is"+identifier+"Available" for identifier in UIA_control_pattern_identifers ]

def get_property_by_id(UIAElement, property_identifier):
    '''
    get property by identifier, return None if fail
    '''
    try:
        UIA_property_identifier = getattr(UIA_wrapper, "UIA_"+property_identifier+"PropertyId")
    except AttributeError:
        LOGGER.warn("This property identifier is not support: %s, cannot get it from UIA typelib" % property_identifier)
        return None
    
    property_value = UIAElement.GetCurrentPropertyValue(UIA_property_identifier)
    if property_value is None:
        LOGGER.warn("This property:%s is not supported by this UIAElment" % property_identifier)
    return property_value
    
def get_pattern_by_id(UIAElement, pattern_identifier):
    '''
    get pattern by identifier, return None if fail
    '''
    try:
        UIA_pattern_identifier = getattr(UIA_wrapper, "UIA_"+pattern_identifier+"Id")
        UIA_pattern_interface = getattr(UIA_wrapper, "IUIAutomation"+pattern_identifier)
    except AttributeError:
        LOGGER.error("This pattern identifier is not support: %s, cannot get it from UIA typelib" % pattern_identifier)
        return None
    
    pattern = UIAElement.GetCurrentPatternAs(UIA_pattern_identifier, UIA_pattern_interface._iid_)
    if pattern is None:
        LOGGER.warn("This pattern:%s is not supported by this UIAElment" % property_identifier)
        return None
    return POINTER(UIA_pattern_interface)(pattern)
    
