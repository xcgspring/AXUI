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
