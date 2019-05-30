.. _`AXUI introduce`:

=========================
AXUI introduce
=========================

:Page Status: Development
:Last Reviewed: 


AXUI philosophy
=========================

Due to various reasons, writing and maintaining UI automation tools can easily turn into a time consuming and unpleasant task.  As a result, it can become hard to reach predefined goals, and eventually the person doing UI automation give up and leave other people with a bad impression. 

Let's have a summary of these reasons:

1. UI is hard for programmers, GUI provide a good/direct interface for people, but not for programmers.  On the contrary, a Command Line Interface (CLI) is easier for programmers to use.

   Controlling a UI is requires inter-process communication.  Typical steps are:
   
   1. find the target UI with some UI special features
   2. control process/scripts send a request to UI
   3. check for response/state
   
   Potential problems in the steps above are:
   
   - UI features used to find GUIs are not user friendly, some features are not visible or have no meaning
   - UI control requests are not user friendly, like a mouse/keyboard/touch event
   - UI could have lots of responses under different condition (UI change/no change/long time response/hang/crash), need to handle all of them

2. Tool support for UI automation is not easy to use, especially for PC platform because there are many UI frameworks on PCs, causing
   many problems for various UI automation tools:
   
   - Different tools use different flavours of programming language styles.
   - Some tools are not powerful enough, but there is no way to extend the functionality of the tools.
   - There are a lot of tools, but experience is required to select the proper tool to use.
   
   .. note::
   
    There are a lot of good tools emerging, like `selenium <https://github.com/SeleniumHQ/selenium>`_ for web test automation, `appium <https://github.com/appium>`_ for smartphone automation

3. Testers lack of programming skills to make test scripts robust and easy to maintain.
   Testers are responsible for test design and test execution.
   Thus, testers might not have enough coding skills to use complex libraries.
   Automation tools should be easy for testers to use, and let testers focus their energy on improving test cases.
      
AXUI is a collection of solutions for these problems::

1. AXUI provides a plug-in mechanism for automation guy to extend support for different UI
2. AXUI provides an unified, easy to use python interface for use in test scripts
3. AXUI separates UI logic from test scripts, making test scripts more readable and easier to maintain
4. AXUI provides mechanism to handle auto met UI automation issues, like UI response time 

To summarize, the purpose of AXUI is to close gaps between testers and UI automation technologies.

AXUI structure
================

AXUI basically includes four modules: 
- XML module to parse ``app map`` 
- driver module to manage different drivers 
- interface module to provide testers an easy to use API 
- core module provides basic functions used by other modules

.. image:: static/AXUI_structure.PNG
   :scale: 50 %

AXUI Technology Details
================================

This section gives a brief introduction to some main features of AXUI

Separate UI logic from test script
--------------------------------------

UI automation technologies often use a formatted string as identifier to find UI element, 
test scripts could contain a lot of these strings, makes scripts harder to understand and maintain.
AXUI separate these strings to a standalone XML file, we usually create a XML file for one app, and thus we normally call this XML file an ``app map``
An ``app map`` is just like a header file containing definitions, so scripts can reuse the definitions in ``app map``, no need to  string in scripts.

Here is a sample ``app map`` for Windows Media Player::

    <AXUI:app_map xmlns:AXUI="AXUI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="AXUI AXUI_app_map.xsd">

        <AXUI:funcs>
            <AXUI:func name="wmplayer_start" description="">
                <AXUI:step type="CLI" cmd='"C:\Program Files\Windows Media Player\wmplayer.exe"'/>
            </AXUI:func>
            
            <AXUI:func name="wmplayer_stop" description="">
                <AXUI:step type="GUI" cmd='wmplayer_Window.WindowPattern.Close'/>
            </AXUI:func>
            
            <AXUI:func name="wmplayer_ctrl_o" description="">
                <AXUI:step type="GUI" cmd="wmplayer_Window.keyboard.Input '^o'" />
            </AXUI:func>
            
            <AXUI:func name="open_dialog_stop" description="">
                <AXUI:step type="GUI" cmd="wmplayer_Window.Open_Dialog.WindowPattern.Close"/>
            </AXUI:func>
        </AXUI:funcs>
        
        <AXUI:UI_elements>
            <AXUI:Root_element name="desktop"/>
            
            <AXUI:UI_element name="wmplayer_Window" parent="desktop" identifier="Name='Windows Media Player' OR Name='Now Playing' AND LocalizedControlType='window'" start_func="wmplayer_start" stop_func="wmplayer_stop">
                <AXUI:UI_element name="Open_Dialog" identifier="Name='Open' AND LocalizedControlType='dialog'" start_func="wmplayer_ctrl_o" stop_func="open_dialog_stop">
                    <AXUI:UI_element name="FileName_ComboBox" identifier="Name='File name:' AND LocalizedControlType='combo box'">
                        <AXUI:UI_element name="FileName_Edit" identifier="Name='File name:' AND LocalizedControlType='edit'"/>
                    </AXUI:UI_element>
                    <AXUI:UI_element name="Open_Button" identifier="Name='Open' AND LocalizedControlType='button' AND Index=2"/>
                </AXUI:UI_element>
            </AXUI:UI_element>
        </AXUI:UI_elements>
        
    </AXUI:app_map>


plug-in mechanism to extend support for different UI
-----------------------------------------------------

AXUI provide a plug-in mechanism to support extend other UI automation technologies to AXUI,
See :ref:`extend AXUI` 

other supports for UI automation
-----------------------------------------------------

AXUI provide other functions may used in UI automation, 

- timeout mechanism to handle UI response time
- image compare for UI verification
- screenshot for every UI operation
- multiple languages support for internationalization (TODO, which means I will never do it :) )

AXUI interface
===============

AXUI restructure the original UI API into two parts, common operations like UI search is taken into AXUI internal, user should use ``app map`` to search UI element,
UI element specified operations like button invoke, set editor value is ported out directly, user can use original API to operate the UI element after UI element is found,
so AXUI can make code disciplined while not reducing the power of original API.

AXUI native API:

- for configuration, ``AXUI.Config(config_file)``, also see :ref:`config AXUI`
- for UIElement checking, ``AXUI.assertIsValid(element, msg)``, also see :ref:`valid AXUI element`
- for AppMap control, ``AXUI.AppMap``, also see :ref:`AXUI AppMap`

Driver special API, mostly AXUI keep original API, for detail usage, you could refer original API documents:

- for windows, check `windows native UIAutomation Client API <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx>`_
- for selenium, check `selenium project <https://github.com/SeleniumHQ/selenium>`_
- for appnium, check `appium project <https://github.com/appium/appium>`_

a simple example
==================

Let's have a simple demo about how to control wmplayer to play back a media file on one 32bit windows machine::

1. Environment prepare
 - First to use AXUI, you need install python environment, prefer python 2.7 (TODO, support python 3 :) )
 - Install AXUI
 - Install ``comtypes`` as windows driver needs this library
2. Write a appmap, like upper example, also see :ref:`AXUI AppMap`
3. Write a config file, usually you can modify the default config file, also see :ref:`config AXUI`
4. Write a script like below::

    ###########################################################
    #prepare part
    ###########################################################
    import AXUI

    config_file = "windows.cfg"             #config file name, abs path needed
    app_map = "windows_media_player.xml"    #app map name, just need a file name, path not needed

    AXUI.Config(config_file)                #load the config file
    appmap = AXUI.AppMap(app_map)           #load the appmap
    
    ############################################################
    #action part, now you can do the UI actions, here we open a media file
    ############################################################
    media_file = ""                         #your media file need to open
    
    #set the media file path to wmplayer open dialog file name edit
    appmap.wmplayer_Window.Open_Dialog.FileName_ComboBox.FileName_Edit.ValuePattern.SetValue(media_file)
    
    #press the open button
    appmap.wmplayer_Window.Open_Dialog.Open_Button.InvokePattern.Invoke()
     
5. Run this script as below, and listen the music::
    
    python script_name.py
