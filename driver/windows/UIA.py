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
import AXUI.logger as AXUI_logger
import ctypes

LOGGER = AXUI_logger.get_logger()

class UIAException(Exception):
    pass

UIA_type_lib_IID = '{944DE083-8FB8-45CF-BCB7-C477ACB2F897}'
#generate UIA python wrapper
UIA_wrapper = GetModule((UIA_type_lib_IID, 1, 0))
#create object of IUIAutomation interface
for interface_id in [("IUIAutomation2", "CUIAutomation8"), ("IUIAutomation", "CUIAutomation")]:
    IUIAutomation = getattr(UIA_wrapper, interface_id[0], None)
    CUIAutomation = getattr(UIA_wrapper, interface_id[1], None)
    if IUIAutomation is not None:
        IUIAutomation_object = CreateObject(CUIAutomation, None, None, IUIAutomation)
        break

##############################
#UI Automation Enumerations
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee671210(v=vs.85).aspx
##############################
UIA_enums = {
"ActiveEnd"                 : {
    "ActiveEnd_None"                    : None,
    "ActiveEnd_Start"                   : None,
    "ActiveEnd_End"                     : None 
    },
"AnimationStyle"            : {
    "AnimationStyle_LasVegasLights"     : None, 
    "AnimationStyle_BlinkingBackground" : None,
    "AnimationStyle_SparkleText"        : None,
    "AnimationStyle_MarchingBlackAnt"   : None,
    "AnimationStyle_MarchingRedAnts"    : None,
    "AnimationStyle_Shimmer"            : None,
    "AnimationStyle_Other"              : None 
    },
"AsyncContentLoadedState"   : {
    "AsyncContentLoadedState_Beginning" : None,
    "AsyncContentLoadedState_Progress"  : None,
    "AsyncContentLoadedState_Completed" : None
    },
"AutomationElementMode"     : {
    "AutomationElementMode_None"        : None,
    "AutomationElementMode_Full"        : None
    },
"AutomationIdentifierType"  : {
    "AutomationIdentifierType_Property" : None,
    "AutomationIdentifierType_Pattern"  : None,
    "AutomationIdentifierType_Event"    : None,
    "AutomationIdentifierType_ControlType"      : None,
    "AutomationIdentifierType_TextAttribute"    : None
    },
"BulletStyle"               : {
    "BulletStyle_None"                  : None,
    "BulletStyle_HollowRoundBullet"     : None,
    "BulletStyle_FilledRoundBullet"     : None,
    "BulletStyle_HollowSquareBullet"    : None,
    "BulletStyle_FilledSquareBullet"    : None,
    "BulletStyle_DashBullet"            : None,
    "BulletStyle_Other"                 : None
    },
"CapStyle"                  : {
    "CapStyle_None"                     : None,
    "CapStyle_SmallCap"                 : None,
    "CapStyle_AllCap"                   : None,
    "CapStyle_AllPetiteCaps"            : None,
    "CapStyle_PetiteCaps"               : None,
    "CapStyle_Unicase"                  : None,
    "CapStyle_Titling"                  : None,
    "Other"                             : None
    },
"CaretBidiMode"             : {
    "CaretBidiMode_LTR"                 : None,
    "CaretBidiMode_RTL"                 : None
    },
"CaretPosition"             : {
    "CaretPosition_Unknown"             : None,
    "CaretPosition_EndOfLine"           : None,
    "CaretPosition_BeginningOfLine"     : None
    },
"ConditionType"             : {
    "ConditionType_True"                : None,
    "ConditionType_False"               : None,
    "ConditionType_Property"            : None,
    "ConditionType_And"                 : None,
    "ConditionType_Or"                  : None,
    "ConditionType_Not"                 : None
    },
"DockPosition"              : {
    "DockPosition_Top"                  : None,
    "DockPosition_Left"                 : None,
    "DockPosition_Bottom"               : None,
    "DockPosition_Right"                : None,
    "DockPosition_Fill"                 : None,
    "DockPosition_None"                 : None
    },
"EventArgsType"             : {
    "EventArgsType_Simple"              : None,
    "EventArgsType_PropertyChanged"     : None,
    "EventArgsType_StructureChanged"    : None,
    "EventArgsType_AsyncContentLoaded"  : None,
    "EventArgsType_WindowClosed"        : None
    },
"ExpandCollapseState"       : {
    "ExpandCollapseState_Collapsed"     : None,
    "ExpandCollapseState_Expanded"      : None,
    "ExpandCollapseState_PartiallyExpanded" : None,
    "ExpandCollapseState_LeafNode"      : None
    },
"FlowDirections"            : {
    "FlowDirections_Default"            : None,
    "FlowDirections_RightToLeft"        : None,
    "FlowDirections_BottomToTop"        : None,
    "FlowDirections_Vertical"           : None
    },
"HorizontalTextAlignmentEnum" : {
    "HorizontalTextAlignment_Left"      : None,
    "HorizontalTextAlignment_Centered"  : None,
    "HorizontalTextAlignment_Right"     : None,
    "HorizontalTextAlignment_Justified" : None
    },
"LiveSetting"               : {
    "LiveSetting_Off"                   : None,
    "LiveSetting_Polite"                : None,
    "LiveSetting_Assertive"             : None
    },
"NavigateDirection"         : {
    "NavigateDirection_Parent"          : None,
    "NavigateDirection_NextSibling"     : None,
    "NavigateDirection_PreviousSibling" : None,
    "NavigateDirection_FirstChild"      : None,
    "NavigateDirection_LastChild"       : None
    },
"NormalizeState"            : {
    "NormalizeState_None"               : None,
    "NormalizeState_View"               : None,
    "NormalizeState_Custom"             : None
    },
"OrientationType"           : {
    "OrientationType_None"              : None,
    "OrientationType_Horizontal"        : None,
    "OrientationType_Vertical"          : None
    },
"OutlineStyles"             : {
    "OutlineStyles_None"                : None,
    "OutlineStyles_Outline"             : None,
    "OutlineStyles_Shadow"              : None,
    "OutlineStyles_Engraved"            : None,
    "OutlineStyles_Embossed"            : None
    },
"PropertyConditionFlags"    : {
    "PropertyConditionFlags_None"       : None,
    "PropertyConditionFlags_IgnoreCase" : None
    },
"ProviderOptions"           : {
    "ProviderOptions_ClientSideProvider"    : None,
    "ProviderOptions_HasNativeIAccessible"  : None,
    "ProviderOptions_NonClientAreaProvider" : None,
    "ProviderOptions_OverrideProvider"      : None,
    "ProviderOptions_ProviderOwnsSetFocus"  : None,
    "ProviderOptions_RefuseNonClientSupport": None,
    "ProviderOptions_ServerSideProvider"    : None,
    "ProviderOptions_UseClientCoordinates"  : None,
    "ProviderOptions_UseComThreading"       : None
    },
"ProviderType"              : {
    "ProviderType_BaseHwnd"                 : None,
    "ProviderType_Proxy"                    : None,
    "ProviderType_NonClientArea"            : None
    },
"RowOrColumnMajor"          : {
    "RowOrColumnMajor_RowMajor"             : None,
    "RowOrColumnMajor_ColumnMajor"          : None,
    "RowOrColumnMajor_Indeterminate"        : None
    },
"ScrollAmount"              : {
    "ScrollAmount_LargeDecrement"           : None,
    "ScrollAmount_SmallDecrement"           : None,
    "ScrollAmount_NoAmount"                 : None,
    "ScrollAmount_LargeIncrement"           : None,
    "ScrollAmount_SmallIncrement"           : None
    },
"StructureChangeType"       : {
    "StructureChangeType_ChildAdded"        : None,
    "StructureChangeType_ChildRemoved"      : None,
    "StructureChangeType_ChildrenInvalidated" : None,
    "StructureChangeType_ChildrenBulkAdded" : None,
    "StructureChangeType_ChildrenBulkRemoved" : None,
    "StructureChangeType_ChildrenReordered" : None
    },
"SupportedTextSelection"    : {
    "SupportedTextSelection_Multiple"       : None,
    "SupportedTextSelection_None"           : None,
    "SupportedTextSelection_Single"         : None
    },
"SynchronizedInputType"     : {
    "SynchronizedInputType_KeyUp"           : None,
    "SynchronizedInputType_KeyDown"         : None,
    "SynchronizedInputType_LeftMouseUp"     : None,
    "SynchronizedInputType_LeftMouseDown"   : None,
    "SynchronizedInputType_RightMouseUp"    : None,
    "SynchronizedInputType_RightMouseDown"  : None
    },
"TextDecorationLineStyle"   : {
    "TextDecorationLineStyle_None"          : None,
    "TextDecorationLineStyle_Single"        : None,
    "TextDecorationLineStyle_WordsOnly"     : None,
    "TextDecorationLineStyle_Double"        : None,
    "TextDecorationLineStyle_Dot"           : None,
    "TextDecorationLineStyle_Dash"          : None,
    "TextDecorationLineStyle_DashDot"       : None,
    "TextDecorationLineStyle_DashDotDot"    : None,
    "TextDecorationLineStyle_Wavy"          : None,
    "TextDecorationLineStyle_ThickSingle"   : None,
    "TextDecorationLineStyle_DoubleWavy"    : None,
    "TextDecorationLineStyle_ThickWavy"     : None,
    "TextDecorationLineStyle_LongDash"      : None,
    "TextDecorationLineStyle_ThickDash"     : None,
    "TextDecorationLineStyle_ThickDashDot"  : None,
    "TextDecorationLineStyle_ThickDashDotDot" : None,
    "TextDecorationLineStyle_ThickDot"      : None,
    "TextDecorationLineStyle_ThickLongDash" : None,
    "TextDecorationLineStyle_Other"         : None
    },
"TextEditChangeType"        : {
    "TextEditChangeType_None"               : None,
    "TextEditChangeType_AutoCorrect"        : None,
    "TextEditChangeType_Composition"        : None,
    "TextEditChangeType_CompositionFinalized" : None
    },
"TextPatternRangeEndpoint"  : {
    "TextPatternRangeEndpoint_Start"        : None,
    "TextPatternRangeEndpoint_End"          : None
    },
"TextUnit"                  : {
    "TextUnit_Character"                    : None,
    "TextUnit_Format"                       : None,
    "TextUnit_Word"                         : None,
    "TextUnit_Line"                         : None,
    "TextUnit_Paragraph"                    : None,
    "TextUnit_Page"                         : None,
    "TextUnit_Document"                     : None
    },
"ToggleState"               : {
    "ToggleState_Off"                       : None,
    "ToggleState_On"                        : None,
    "ToggleState_Indeterminate"             : None
    },
"TreeScope"                 : {
    "TreeScope_Element"                     : None,
    "TreeScope_Children"                    : None,
    "TreeScope_Descendants"                 : None,
    "TreeScope_Parent"                      : None,
    "TreeScope_Ancestors"                   : None,
    "TreeScope_Subtree"                     : None
    },
"UIAutomationType"          : {
    "UIAutomationType_Int"                  : None,
    "UIAutomationType_Bool"                 : None,
    "UIAutomationType_String"               : None,
    "UIAutomationType_Double"               : None,
    "UIAutomationType_Point"                : None,
    "UIAutomationType_Rect"                 : None,
    "UIAutomationType_Element"              : None, 
    "UIAutomationType_Array"                : None,
    "UIAutomationType_Out"                  : None,
    "UIAutomationType_IntArray"             : None,
    "UIAutomationType_BoolArray"            : None,
    "UIAutomationType_StringArray"          : None,
    "UIAutomationType_DoubleArray"          : None,
    "UIAutomationType_PointArray"           : None,
    "UIAutomationType_RectArray"            : None,
    "UIAutomationType_ElementArray"         : None,
    "UIAutomationType_OutInt"               : None,
    "UIAutomationType_OutBool"              : None,
    "UIAutomationType_OutString"            : None,
    "UIAutomationType_OutDouble"            : None,
    "UIAutomationType_OutPoint"             : None,
    "UIAutomationType_OutRect"              : None,
    "UIAutomationType_OutElement"           : None,
    "UIAutomationType_OutIntArray"          : None,
    "UIAutomationType_OutBoolArray"         : None,
    "UIAutomationType_OutStringArray"       : None,
    "UIAutomationType_OutDoubleArray"       : None,
    "UIAutomationType_OutPointArray"        : None,
    "UIAutomationType_OutRectArray"         : None,
    "UIAutomationType_OutElementArray"      : None
    },
"WindowInteractionState"    : {
    "WindowInteractionState_Running"        : None,
    "WindowInteractionState_Closing"        : None,
    "WindowInteractionState_ReadyForUserInteraction" : None,
    "WindowInteractionState_BlockedByModalWindow"    : None,
    "WindowInteractionState_NotResponding"  : None
    },
"WindowVisualState"         : {
    "WindowVisualState_Normal"              : None,
    "WindowVisualState_Maximized"           : None,
    "WindowVisualState_Minimized"           : None
    },
"ZoomUnit"                  : {
    "ZoomUnit_NoAmount"                     : None,
    "ZoomUnit_LargeDecrement"               : None,
    "ZoomUnit_SmallDecrement"               : None,
    "ZoomUnit_LargeIncrement"               : None,
    "ZoomUnit_SmallIncrement"               : None
    },
}

#check if enum exist in current version UIA namespace
#set the value if exist
for enum in UIA_enums.items():
    enum_name = enum[0]
    enum_contents = enum[1]
    #check if enum name in current UIA namespace
    enum_name_type = getattr(UIA_wrapper, enum_name, None)
    if enum_name_type is not ctypes.c_int:
        #enum type should be c_int in UIA wrapper namespace
        #skip this enum if enum type is not c_int
        LOGGER.warn("enum: %s not exist in UIA namespace" % enum_name)
        continue
    
    for enum_content_name in enum_contents:
        enum_content_value = getattr(UIA_wrapper, enum_content_name, None)
        #set the value to UIA_enums dict
        UIA_enums[enum_name][enum_content_name] = enum_content_value

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
    
#build map for property identifiers
UIA_automation_element_property_identifers_mapping = {}
for property_identifier in UIA_automation_element_property_identifers:
    value = getattr(UIA_wrapper, "UIA_"+property_identifier+"PropertyId", None)
    if value is None:
        LOGGER.warn("property identifier: %s not supported by current UIA version" % property_identifier)
        continue
        
    UIA_automation_element_property_identifers_mapping[property_identifier] = value
    
    
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
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentAnnotationTypeName',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CurrentAuthor',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CurrentDateTime',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CurrentTarget',
              ( 'out', 'POINTER(IUIAutomationElement)', 'retVal' )),
    ('property', 'CachedAnnotationTypeId',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedAnnotationTypeName',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CachedAuthor',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CachedDateTime',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CachedTarget',
              ( 'out', 'POINTER(IUIAutomationElement)', 'retVal' )),
],
"DockPattern"               : [
    ('method', 'SetDockPosition',
              ( 'in', 'DockPosition', 'dockPos' )),
    ('property', 'CurrentDockPosition',
              ( 'out', 'DockPosition', 'retVal' )),
    ('property', 'CachedDockPosition',
              ( 'out', 'DockPosition', 'retVal' )),
],
"DragPattern"               : [
    ('property', 'CurrentIsGrabbed',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedIsGrabbed',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentDropEffect',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CachedDropEffect',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CurrentDropEffects',
              ( 'out', '_midlSAFEARRAY(BSTR)', 'retVal' )),
    ('property', 'CachedDropEffects',
              ( 'out', '_midlSAFEARRAY(BSTR)', 'retVal' )),
    ('method', 'GetCurrentGrabbedItems',
              ( 'out', 'POINTER(IUIAutomationElementArray)', 'retVal' )),
    ('method', 'GetCachedGrabbedItems',
              ( 'out', 'POINTER(IUIAutomationElementArray)', 'retVal' )),
],
"DropTargetPattern"         : [
    ('property', 'CurrentDropTargetEffect',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CachedDropTargetEffect',
              ( 'out', 'BSTR', 'retVal' )),
    ('property', 'CurrentDropTargetEffects',
              ( 'out', '_midlSAFEARRAY(BSTR)', 'retVal' )),
    ('property', 'CachedDropTargetEffects',
              ( 'out', '_midlSAFEARRAY(BSTR)', 'retVal' )),
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
              ( 'out', 'POINTER(IUIAutomationElement)', 'retVal' )),
    ('property', 'CurrentRow',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentColumn',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentRowSpan',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentColumnSpan',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedContainingGrid',
              ( 'out', 'POINTER(IUIAutomationElement)', 'retVal' )),
    ('property', 'CachedRow',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedColumn',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedRowSpan',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedColumnSpan',
              ( 'out', 'c_int', 'retVal' )),
],
"GridPattern"               : [
    ('method', 'GetItem',
              ( 'in', 'c_int', 'row' ),
              ( 'in', 'c_int', 'column' ),
              ( 'out', 'POINTER(IUIAutomationElement)', 'element' )),
    ('property', 'CurrentRowCount',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentColumnCount',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedRowCount',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedColumnCount',
              ( 'out', 'c_int', 'retVal' )),
],
"InvokePattern"             : [
    ('method', 'Invoke'),
],
"ItemContainerPattern"      : [
    ('method', 'FindItemByProperty',
              ( 'in', 'POINTER(IUIAutomationElement)', 'pStartAfter' ),
              ( 'in', 'c_int', 'propertyId' ),
              ( 'in', 'VARIANT', 'value' ),
              ( 'out', 'POINTER(IUIAutomationElement)', 'pFound' )),
],
"LegacyIAccessiblePattern"  : [
    ('method', 'Select',
              ( 'in', 'c_int', 'flagsSelect' )),
    ('method', 'DoDefaultAction'),
    ('method', 'SetValue',
              ( 'in', 'WSTRING', 'szValue' )),
    ('property', 'CurrentChildId',
              ( 'out', 'c_int', 'pRetVal' )),
    ('property', 'CurrentName',
              ( 'out', 'BSTR', 'pszName' )),
    ('property', 'CurrentValue',
              ( 'out', 'BSTR', 'pszValue' )),
    ('property', 'CurrentDescription',
              ( 'out', 'BSTR', 'pszDescription' )),
    ('property', 'CurrentRole',
              ( 'out', 'c_ulong', 'pdwRole' )),
    ('property', 'CurrentState',
              ( 'out', 'c_ulong', 'pdwState' )),
    ('property', 'CurrentHelp',
              ( 'out', 'BSTR', 'pszHelp' )),
    ('property', 'CurrentKeyboardShortcut',
              ( 'out', 'BSTR', 'pszKeyboardShortcut' )),
    ('method', 'GetCurrentSelection',
              ( 'out', 'POINTER(IUIAutomationElementArray)', 'pvarSelectedChildren' )),
    ('property', 'CurrentDefaultAction',
              ( 'out', 'BSTR', 'pszDefaultAction' )),
    ('property', 'CachedChildId',
              ( 'out', 'c_int', 'pRetVal' )),
    ('property', 'CachedName',
              ( 'out', 'BSTR', 'pszName' )),
    ('property', 'CachedValue',
              ( 'out', 'BSTR', 'pszValue' )),
    ('property', 'CachedDescription',
              ( 'out', 'BSTR', 'pszDescription' )),
    ('property', 'CachedRole',
              ( 'out', 'c_ulong', 'pdwRole' )),
    ('property', 'CachedState',
              ( 'out', 'c_ulong', 'pdwState' )),
    ('property', 'CachedHelp',
              ( 'out', 'BSTR', 'pszHelp' )),
    ('property', 'CachedKeyboardShortcut',
              ( 'out', 'BSTR', 'pszKeyboardShortcut' )),
    ('method', 'GetCachedSelection',
              ( 'out', 'POINTER(IUIAutomationElementArray)', 'pvarSelectedChildren' )),
    ('property', 'CachedDefaultAction',
              ( 'out', 'BSTR', 'pszDefaultAction' )),
    ('method', 'GetIAccessible',
              ( 'out', 'POINTER(IAccessible)', 'ppAccessible' )),
],
"MultipleViewPattern"       : [
    ('method', 'GetViewName',
              ( 'in', 'c_int', 'view' ),
              ( 'out', 'BSTR', 'name' )),
    ('method', 'SetCurrentView',
              ( 'in', 'c_int', 'view' )),
    ('property', 'CurrentCurrentView',
              ( 'out', 'c_int', 'retVal' )),
    ('method', 'GetCurrentSupportedViews',
              ( 'out', '_midlSAFEARRAY(c_int)', 'retVal' )),
    ('property', 'CachedCurrentView',
              ( 'out', 'c_int', 'retVal' )),
    ('method', 'GetCachedSupportedViews',
              ( 'out', '_midlSAFEARRAY(c_int)', 'retVal' )),
],
"ObjectModelPattern"        : [
    ('method', 'GetUnderlyingObjectModel',
              ( 'out', 'POINTER(IUnknown)', 'retVal' )),
],
"RangeValuePattern"         : [
    ('method', 'SetValue',
              ( 'in', 'c_double', 'val' )),
    ('property', 'CurrentValue',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentIsReadOnly',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CurrentMaximum',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentMinimum',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentLargeChange',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentSmallChange',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CachedValue',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CachedIsReadOnly',
              ( 'out', 'c_int', 'retVal' )),
    ('property', 'CachedMaximum',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CachedMinimum',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CachedLargeChange',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CachedSmallChange',
              ( 'out', 'c_double', 'retVal' )),
],
"ScrollItemPattern"         : [
    ('method', 'ScrollIntoView'),
],
"ScrollPattern"             : [
    ('method', 'Scroll',
              ( 'in', 'ScrollAmount', 'horizontalAmount' ),
              ( 'in', 'ScrollAmount', 'verticalAmount' )),
    ('method', 'SetScrollPercent',
              ( 'in', 'c_double', 'horizontalPercent' ),
              ( 'in', 'c_double', 'verticalPercent' )),
    ('property', 'CurrentHorizontalScrollPercent',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentVerticalScrollPercent',
              ( 'out', 'c_double', 'retVal' )),
    ('property', 'CurrentHorizontalViewSize',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentVerticalViewSize',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentHorizontallyScrollable',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentVerticallyScrollable',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedHorizontalScrollPercent',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedVerticalScrollPercent',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedHorizontalViewSize',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedVerticalViewSize',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedHorizontallyScrollable',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedVerticallyScrollable',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
],
"SelectionItemPattern"      : [
    ('method', 'Select'),
    ('method', 'AddToSelection'),
    ('method', 'RemoveFromSelection'),
    ('property', 'CurrentIsSelected',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentSelectionContainer',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
    ('property', 'CachedIsSelected',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedSelectionContainer',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'retVal' )),
],
"SelectionPattern"          : [
    ('method', 'GetCurrentSelection',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('property', 'CurrentCanSelectMultiple',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentIsSelectionRequired',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('method', 'GetCachedSelection',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('property', 'CachedCanSelectMultiple',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedIsSelectionRequired',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
],
"SpreadsheetPattern"        : [
    ('method', 'GetItemByName',
              ( 'in', 'BSTR', 'name' ),
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'element' )),
],
"SpreadsheetItemPattern"    : [
    ('property', 'CurrentFormula',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('method', 'GetCurrentAnnotationObjects',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCurrentAnnotationTypes',
              ( 'out', 'POINTER(_midlSAFEARRAY(c_int))', 'retVal' )),
    ('property', 'CachedFormula',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('method', 'GetCachedAnnotationObjects',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCachedAnnotationTypes',
              ( 'out', 'POINTER(_midlSAFEARRAY(c_int))', 'retVal' )),
],
"StylesPattern"             : [
    ('property', 'CurrentStyleId',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentStyleName',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentFillColor',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentFillPatternStyle',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentShape',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CurrentFillPatternColor',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentExtendedProperties',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('method', 'GetCurrentExtendedPropertiesAsArray',
              ( 'out', 'POINTER(POINTER(ExtendedProperty))', 'propertyArray' ),
              ( 'out', 'POINTER(c_int)', 'propertyCount' )),
    ('property', 'CachedStyleId',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedStyleName',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedFillColor',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedFillPatternStyle',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedShape',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('property', 'CachedFillPatternColor',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedExtendedProperties',
              ( 'out', 'POINTER(BSTR)', 'retVal' )),
    ('method', 'GetCachedExtendedPropertiesAsArray',
              ( 'out', 'POINTER(POINTER(ExtendedProperty))', 'propertyArray' ),
              ( 'out', 'POINTER(c_int)', 'propertyCount' )),
],
"SynchronizedInputPattern"  : [
    ('method', 'StartListening',
              ( 'in', 'SynchronizedInputType', 'inputType' )),
    ('method', 'Cancel'),
],
"TableItemPattern"          : [
    ('method', 'GetCurrentRowHeaderItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCurrentColumnHeaderItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCachedRowHeaderItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCachedColumnHeaderItems',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
],
"TablePattern"              : [
    ('method', 'GetCurrentRowHeaders',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCurrentColumnHeaders',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('property', 'CurrentRowOrColumnMajor',
              ( 'out', 'POINTER(RowOrColumnMajor)', 'retVal' )),
    ('method', 'GetCachedRowHeaders',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('method', 'GetCachedColumnHeaders',
              ( 'out', 'POINTER(POINTER(IUIAutomationElementArray))', 'retVal' )),
    ('property', 'CachedRowOrColumnMajor',
              ( 'out', 'POINTER(RowOrColumnMajor)', 'retVal' )),
],
"TextChildPattern"          : [
    ('property', 'TextContainer',
              ( 'out', 'POINTER(POINTER(IUIAutomationElement))', 'container' )),
    ('property', 'TextRange',
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
],
"TextEditPattern"           : None,
"TextPattern"               : [
    ('method', 'RangeFromPoint',
              ( 'in', 'tagPOINT', 'pt' ),
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
    ('method', 'RangeFromChild',
              ( 'in', 'POINTER(IUIAutomationElement)', 'child' ),
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
    ('method', 'GetSelection',
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRangeArray))', 'ranges' )),
    ('method', 'GetVisibleRanges',
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRangeArray))', 'ranges' )),
    ('property', 'DocumentRange',
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
    ('property', 'SupportedTextSelection',
              ( 'out', 'POINTER(SupportedTextSelection)', 'SupportedTextSelection' )),
],
"TextPattern2"              : [
    ('method', 'RangeFromAnnotation',
              ( 'in', 'POINTER(IUIAutomationElement)', 'annotation' ),
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
    ('method', 'GetCaretRange',
              ( 'out', 'POINTER(c_int)', 'isActive' ),
              ( 'out', 'POINTER(POINTER(IUIAutomationTextRange))', 'range' )),
],
"TogglePattern"             : [
    ('method', 'Toggle'),
    ('property', 'CurrentToggleState',
              ( 'out', 'POINTER(ToggleState)', 'retVal' )),
    ('property', 'CachedToggleState',
              ( 'out', 'POINTER(ToggleState)', 'retVal' )),
],
"TransformPattern"          : [
    ('method', 'Move',
              ( 'in', 'c_double', 'x' ),
              ( 'in', 'c_double', 'y' )),
    ('method', 'Resize',
              ( 'in', 'c_double', 'width' ),
              ( 'in', 'c_double', 'height' )),
    ('method', 'Rotate',
              ( 'in', 'c_double', 'degrees' )),
    ('property', 'CurrentCanMove',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentCanResize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentCanRotate',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedCanMove',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedCanResize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedCanRotate',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
],
"TransformPattern2"         : [
    ('method', 'Zoom',
              ( 'in', 'c_double', 'Zoom' )),
    ('method', 'ZoomByUnit',
              ( 'in', 'ZoomUnit', 'ZoomUnit' )),
    ('property', 'CurrentCanZoom',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedCanZoom',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentZoomLevel',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedZoomLevel',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentZoomMinimum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedZoomMinimum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentZoomMaximum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedZoomMaximum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
],
"ValuePattern"              : [
    ('method', 'SetValue',
              ( 'in', 'c_double', 'val' )),
    ('property', 'CurrentValue',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentIsReadOnly',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentMaximum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentMinimum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentLargeChange',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CurrentSmallChange',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedValue',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedIsReadOnly',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedMaximum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedMinimum',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedLargeChange',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
    ('property', 'CachedSmallChange',
              ( 'out', 'POINTER(c_double)', 'retVal' )),
],
"VirtualizedItemPattern"    : [
    ('method', 'Realize'),
],
"WindowPattern"             : [
    ('method', 'Close'),
    ('method', 'WaitForInputIdle',
              ( 'in', 'c_int', 'milliseconds' ),
              ( 'out', 'POINTER(c_int)', 'success' )),
    ('method', 'SetWindowVisualState',
              ( 'in', 'WindowVisualState', 'state' )),
    ('property', 'CurrentCanMaximize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentCanMinimize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentIsModal',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentIsTopmost',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CurrentWindowVisualState',
              ( 'out', 'POINTER(WindowVisualState)', 'retVal' )),
    ('property', 'CurrentWindowInteractionState',
              ( 'out', 'POINTER(WindowInteractionState)', 'retVal' )),
    ('property', 'CachedCanMaximize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedCanMinimize',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedIsModal',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedIsTopmost',
              ( 'out', 'POINTER(c_int)', 'retVal' )),
    ('property', 'CachedWindowVisualState',
              ( 'out', 'POINTER(WindowVisualState)', 'retVal' )),
    ('property', 'CachedWindowInteractionState',
              ( 'out', 'POINTER(WindowInteractionState)', 'retVal' )),
],
}

#Control Pattern Identifiers
UIA_control_pattern_identifers = UIA_control_pattern_interfaces.keys()

#Control Pattern Availability Property Identifiers
UIA_control_pattern_availability_property_identifiers = \
[ "Is"+identifier+"Available" for identifier in UIA_control_pattern_identifers ]

def get_property_by_id(UIAElement, property_identifier):
    '''
    get property by identifier, return None if fail
    '''
    if property_identifier in UIA_automation_element_property_identifers_mapping:
        property_value = UIAElement.GetCurrentPropertyValue(UIA_property_identifier)
        if property_value is None:
            LOGGER.warn("This property:%s is not supported by this UIAElment" % property_identifier)
        return property_value
    else:
        LOGGER.warn("This property identifier is not support: %s, cannot get it from UIA typelib" % property_identifier)
        return None
    
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
    return ctypes.POINTER(UIA_pattern_interface)(pattern)
    
