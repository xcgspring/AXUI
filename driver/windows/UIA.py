'''
Use comtypes to generate python wrapper for windows native UIA API

Comtypes: 
    https://github.com/enthought/comtypes
Windows native UIA API: 
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee671216(v=vs.85).aspx
'''

from comtypes.client import GetModule, CreateObject

UIA_type_lib_IID = '{944DE083-8FB8-45CF-BCB7-C477ACB2F897}'
#generate UIA python wrapper
UIA_wrapper = GetModule((UIA_type_lib_IID, 1, 0))
#create object of IUIAutomation
IUIAutomation_object = CreateObject(UIA_wrapper.CUIAutomation, None, None, UIA_wrapper.IUIAutomation)

#UIA Automation Element Property Identifiers
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx
#You can check element property using inspect.exe
#http://msdn.microsoft.com/en-us/library/windows/desktop/dd318521(v=vs.85).aspx
UIA_property_identifers_mapping = {
    "AcceleratorKey":   UIA_wrapper.UIA_AcceleratorKeyPropertyId,
    "AccessKey":        UIA_wrapper.UIA_AccessKeyPropertyId,
    "AriaProperties":   UIA_wrapper.UIA_AriaPropertiesPropertyId,
    "AriaRole":         UIA_wrapper.UIA_AriaRolePropertyId,
    "AutomationId":     UIA_wrapper.UIA_AutomationIdPropertyId,
    "BoundingRectangle":UIA_wrapper.UIA_BoundingRectanglePropertyId,
    "ClassName":        UIA_wrapper.UIA_ClassNamePropertyId,
    "ClickablePoint":   UIA_wrapper.UIA_ClickablePointPropertyId,
    "ControllerFor":    UIA_wrapper.UIA_ControllerForPropertyId,
    "ControlType":      UIA_wrapper.UIA_ControlTypePropertyId,
    "Culture":          UIA_wrapper.UIA_CulturePropertyId,
    "DescribedBy":      UIA_wrapper.UIA_DescribedByPropertyId,
    "FlowsFrom":        UIA_wrapper.UIA_FlowsFromPropertyId,
    "FlowsTo":          UIA_wrapper.UIA_FlowsToPropertyId,
    "FrameworkId":      UIA_wrapper.UIA_FrameworkIdPropertyId,
    "HasKeyboardFocus": UIA_wrapper.UIA_HasKeyboardFocusPropertyId,
    "HelpText":         UIA_wrapper.UIA_HelpTextPropertyId,
    "IsContentElement": UIA_wrapper.UIA_IsContentElementPropertyId,
    "IsControlElement": UIA_wrapper.UIA_IsControlElementPropertyId,
    "IsDataValidForForm": UIA_wrapper.UIA_IsDataValidForFormPropertyId,
    "IsEnabled":        UIA_wrapper.UIA_IsEnabledPropertyId,
    "IsKeyboardFocusable":UIA_wrapper.UIA_IsKeyboardFocusablePropertyId,
    "IsOffscreen":      UIA_wrapper.UIA_IsOffscreenPropertyId,
    "IsPassword":       UIA_wrapper.UIA_IsPasswordPropertyId,
    "IsPeripheral":     UIA_wrapper.UIA_IsPeripheralPropertyId,
    "IsRequiredForForm":UIA_wrapper.UIA_IsRequiredForFormPropertyId,
    "ItemStatus":       UIA_wrapper.UIA_ItemStatusPropertyId,
    "ItemType":         UIA_wrapper.UIA_ItemTypePropertyId,
    "LabeledBy":        UIA_wrapper.UIA_LabeledByPropertyId,
    "LiveSetting":      UIA_wrapper.UIA_LiveSettingPropertyId,
    "LocalizedControlType":UIA_wrapper.UIA_LocalizedControlTypePropertyId,
    "Name":             UIA_wrapper.UIA_NamePropertyId,
    "NativeWindowHandle":UIA_wrapper.UIA_NativeWindowHandlePropertyId,
    "OptimizeForVisualContent":UIA_wrapper.UIA_OptimizeForVisualContentPropertyId,
    "Orientation":      UIA_wrapper.UIA_OrientationPropertyId,
    "ProcessId":        UIA_wrapper.UIA_ProcessIdPropertyId,
    "ProviderDescription":UIA_wrapper.UIA_ProviderDescriptionPropertyId,
    "RuntimeId":        UIA_wrapper.UIA_RuntimeIdPropertyId
    }
    
#UIA Control Pattern Identifiers
#http://msdn.microsoft.com/en-us/library/windows/desktop/ee671195(v=vs.85).aspx
UIA_Pattern_identifers_mapping = {
    "Annotation":       UIA_wrapper.UIA_AnnotationPatternId,
    "Dock":             UIA_wrapper.UIA_DockPatternId,
    "Drag":             UIA_wrapper.UIA_DragPatternId,
    "Drop":             UIA_wrapper.UIA_DropTargetPatternId,
    "ExpandCollapse":   UIA_wrapper.UIA_ExpandCollapsePatternId,
    "GridItem":         UIA_wrapper.UIA_GridItemPatternId,
    "Grid":             UIA_wrapper.UIA_GridPatternId,
    "Invoke":           UIA_wrapper.UIA_InvokePatternId,
    "ItemContainer":    UIA_wrapper.UIA_ItemContainerPatternId,
    "LegacyIAccessible":UIA_wrapper.UIA_LegacyIAccessiblePatternId,
    "MultipleView":     UIA_wrapper.UIA_MultipleViewPatternId,
    "ObjectModel":      UIA_wrapper.UIA_ObjectModelPatternId,
    "RangeValue":       UIA_wrapper.UIA_RangeValuePatternId,
    "ScrollItem":       UIA_wrapper.UIA_ScrollItemPatternId,
    "Scroll":           UIA_wrapper.UIA_ScrollPatternId,
    "SelectionItem":    UIA_wrapper.UIA_SelectionItemPatternId,
    "Selection":        UIA_wrapper.UIA_SelectionPatternId,
    "Spreadsheet":      UIA_wrapper.UIA_SpreadsheetPatternId,
    "SpreadsheetItem":  UIA_wrapper.UIA_SpreadsheetItemPatternId,
    "Styles":           UIA_wrapper.UIA_StylesPatternId,
    "SynchronizedInput":UIA_wrapper.UIA_SynchronizedInputPatternId,
    "TableItem":        UIA_wrapper.UIA_TableItemPatternId,
    "Table":            UIA_wrapper.UIA_TablePatternId,
    "TextChild":        UIA_wrapper.UIA_TextChildPatternId,
    "TextEdit":         UIA_wrapper.UIA_TextEditPatternId,
    "Text":             UIA_wrapper.UIA_TextPatternId,
    "Text2":            UIA_wrapper.UIA_TextPattern2Id,
    "Toggle":           UIA_wrapper.UIA_TogglePatternId,
    "Transform":        UIA_wrapper.UIA_TransformPatternId,
    "Transform2":       UIA_wrapper.UIA_TransformPattern2Id,
    "Value":            UIA_wrapper.UIA_ValuePatternId,
    "VirtualizedItem":  UIA_wrapper.UIA_VirtualizedItemPatternId,
    "Window":           UIA_wrapper.UIA_WindowPatternId,
    }
    
