.. _`AXUI built-in drivers`:

=========================
AXUI built-in drivers
=========================

:Page Status: Development
:Last Reviewed: 

AXUI has implement some drivers for common used platforms, this chapter will have a introduce about this three drivers

- windows desktop, based on `windows native UIAutomation Client API <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx>`_
- web, based on `selenium project <https://github.com/SeleniumHQ/selenium>`_
- mobile android/ios, based on `appium project <https://github.com/appium/appium>`_

driver for windows UIAutomation API
====================================

We use `comtypes <https://github.com/enthought/comtypes>`_ to access this windows COM API, 
thus to use AXUI to automate windows UI, you need install `comtypes <https://github.com/enthought/comtypes>`_ first.

Windows UIAutomation API separates operations for different kinds of UI into a set of `control patterns <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684023(v=vs.85).aspx>`_, 
it's recommended to use these patterns to operate target UI,
AXUI expose these patterns to end users, anyway end users should need to have a check of these patterns.

.. note::

 I have tested windows driver on win8.1 and win10,
 
 - it's works well with windows UI framework like win32, winform, WPF, windows store app
 - not works well with Qt framework, UIA recognize all kinds of Qt controls as frames  
 - not support for directX, custom UI controls

UIA identifiers
----------------------

UIA supports `different ways to find UI elements <https://msdn.microsoft.com/en-us/library/windows/desktop/ee671590(v=vs.85).aspx>`_, 
AXUI only uses `FindFisrt <https://msdn.microsoft.com/en-us/library/windows/desktop/ee696029(v=vs.85).aspx>`_ and `FindAll <https://msdn.microsoft.com/en-us/library/windows/desktop/ee696027(v=vs.85).aspx>`_ to find UI element.

For `search scope <https://msdn.microsoft.com/en-us/library/windows/desktop/ee671590(v=vs.85).aspx#SearchScope>`_, AXUI uses `TreeScope_Descendants` as default, only uses `TreeScope_Children` for find element under root element.

Basically, AXUI supports most of UIA `search conditions <https://msdn.microsoft.com/en-us/library/windows/desktop/ee671590(v=vs.85).aspx#Conditions>`_, in a different flavour using AppMap.
The search condition in AppMap has a structure like::

 identifier="<key=value [AND key=value] [OR key=value]>"
 
the identifier key is from `UIA property identifiers <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx>`_, we strip the repeat part and get our AXUI identifier key, like::
 
 UIA_NamePropertyId  -> [UIA_]Name[PropertyId] -> Name 

- single `property condition <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx>`_, like: ``"Name='element_name'"``
- simple and/or condition, like: ``"Name='element_name' AND IsEnabled=True"``, ``"Name='element_name_1' OR Name='element_name_1'"``
- multiple and/or condition, like: ``"Name='element_name_1' OR Name='element_name_1' AND IsEnabled=True"``

.. note::

 Suggest using inspect tool to retrieve UI identifier values

UIA element properties
----------------------

UIA element has properties that we can retrieve and check their values, to get these properties value, we just need to append the property name after the element, just like normal python properties::

 appmap.<element_1>.[element_2]...[element_n].property_name
 
`property_name` is from `UIA property identifiers <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684017(v=vs.85).aspx>`_, just like AXUI identifier key::

 UIA_NamePropertyId  -> [UIA_]Name[PropertyId] -> Name

UIA element patterns
----------------------

As said before, UIA split interfaces for different UI element into different `control patterns <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684023(v=vs.85).aspx>`_, 
AXUI porting these pattern interfaces untouched, you can use these pattern interfaces directly::

 appmap.<element_1>.[element_2]...[element_n].pattern_name.[pattern_method][pattern_property]

Notice pattern_name is from `control patterns <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684023(v=vs.85).aspx>`_, with "IUIAutomation" prefix stripped::

 IUIAutomationValuePattern -> [IUIAutomation]ValuePattern -> ValuePattern

driver for `WebDriver <https://w3c.github.io/webdriver/webdriver-spec.html>`_ compatible projects
===================================================================================================

``selenium webdriver`` and ``appium`` all use a C/S structure to support multiple languages, the client side and server side use `WebDriver <https://w3c.github.io/webdriver/webdriver-spec.html>`_ protocol to communicate with each other.
since ``selenium webdriver`` and ``appium`` already have python clients, we don't reinvent the wheel, but use these python clients to implement our drivers for AXUI

.. note::
 
 Since I only little experience for web UI and mobile UI automation, these driver could be not good to use
 
 Welcome if somebody to write better drivers to replace my reference drivers.

selenium webdriver
-------------------

selenium identifiers
---------------------

All selenium identifiers to search elements is in ``selenium/webdriver/common/by.py``, we can use these identifiers to search elements in AXUI, like::

 identifier="key=value"
 
It's similar with windows driver, but not supports and/or search condition. 
The identifier key is property names of ``By`` class. Like "ID", "XPATH", "TAG_NAME"...
 
selenium properties
---------------------

We can retrieve the selenium element's properties just like normal python properties::

 appmap.<element_1>.[element_2]...[element_n].property_name
 
``property_name`` is same with selenium element property name 

selenium patterns/interfaces
-------------------------------

I have restructured the selenium element methods to different pattern class, so you cannot access selenium element methods directly.
Currently there are 4 pattern interfaces:

``Keyboard`` interface
############################

This interface has one method "input", to replace selenium "send_keys" method.
For input normal keys like [0~9][a~z][A~Z], input directly::
    
    appmap.<element_1>.[element_2]...[element_n].Keyboard.input("123asdfADSD")

For special charactors like "space", "tab", "newline", "F1~F12", 
You use {key_name} to replace them, all support keys in "selenium/webdriver/common/keys".

    appmap.<element_1>.[element_2]...[element_n].Keyboard.input("{space}", "{tab}", "{F1}")

``Mouse`` interface
############################

This interface has one method "left_click", to replace selenium "click" method::

    appmap.<element_1>.[element_2]...[element_n].Mouse.left_click()

``WebUIElementPattern`` interface
##################################

This interface wrap original selenium methods for normal web element::

    interfaces = [
        "submit",
        "clear",

        "is_selected",
        "is_enabled",
        "is_displayed",

        "value_of_css_property",
    ]

Use like::
    
    appmap.<element_1>.[element_2]...[element_n].WebUIElementPattern.is_enabled()
    
``BrowserPattern`` interface
#############################

This interface wrap original selenium methods for browser element::

    interfaces = [
        "get",
        "close",
        "maximize_window",

        "execute_script",
        "execute_async_script",
        "set_script_timeout",

        "back",
        "forward",
        "refresh",

        "get_cookies",
        "get_cookie",
        "delete_cookie",
        "delete_all_cookies",
        "add_cookie",

        "implicitly_wait",
        "set_page_load_timeout",

        "set_window_size",
        "get_window_size",
        "set_window_position",
        "get_window_position",

        "get_log",
    ]

Use like::

    appmap.<element_1>.[element_2]...[element_n].BrowserPattern.get("http:://www.bing.com")
    
.. note::

 I have tested selenium driver with some browsers on windows, seems selenium webdriver has some problems with IE 11.
 
 Suggest use window driver to test IE's UI, windows UIA supports IE pretty well.

appium
-----------------


.. note::

 since I don't have an apple/android environment, the appium driver is not tested
 
 I will be very glad someone can have a test for it :)