.. _`AXUI AppMap`:

=========================
AXUI AppMap
=========================

:Page Status: Development
:Last Reviewed: 

AppMap overview
=========================

AppMap is a key feature of AXUI, use AppMap smart can make your automation task much easier.
Basically, AppMap is to store all changeable UI element features, and provide a consistent AppMap element for use.
Thus, AppMap could reduce the scripts mutability, and make script easier for maintenance.
This feature also provide a direct solution for internationalization. 

We will provide a detail introduce for each part of AppMap below, before that, here provide a sample AppMap containing all parts of AppMap::

    <AXUI:app_map xmlns:AXUI="AXUI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="AXUI AXUI_app_map.xsd">

    <AXUI:variables>
        <AXUI:variable name="" value="" />
    </AXUI:variables>

    <AXUI:includes>
        <AXUI:include name="" path="" />
    </AXUI:includes>

    <AXUI:funcs>
        <AXUI:func name="" description="">
            <AXUI:step type="" cmd=''/>
        </AXUI:func>
    </AXUI:funcs>
    
    <AXUI:UI_elements>
        <AXUI:Root_element name=""/>
        
        <AXUI:UI_element name="" parent="" identifier="" start_func="" stop_func="">
            <AXUI:UI_element name="" identifier="" start_func="">
                <AXUI:UI_element name="" identifier="" />
            </AXUI:UI_element>
        </AXUI:UI_element>
    </AXUI:UI_elements>
    
</AXUI:app_map>


AppMap elements
=====================

Here we have an introduce for each element in AppMap, AppMap will be checked with a pre-defined schema ``AXUI/XML/schemas/AXUI_app_map.xsd``

root element -- AXUI:app_map
----------------------------

``AXUI:app_map`` is the root element of AppMap, it should always be::

    <AXUI:app_map xmlns:AXUI="AXUI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="AXUI AXUI_app_map.xsd">
        ......
    </AXUI:app_map>

AXUI:variables
------------------

``AXUI:variables`` can include multiple ``AXUI:variable`` elements, ``AXUI:variables`` has no attributes.

AXUI:variable
##################

``AXUI:variable`` element provide a dynamic way to change AppMap contents, currently only support change command line in ``AXUI:func`` element

typical usage::

    <AXUI:variables>
        <AXUI:variable name="AppPath" value='"some_app_path"'/>
    </AXUI:variables>

    <AXUI:funcs>
        <AXUI:func name="start_some_element" description="">
            <AXUI:step type="CLI" cmd='{AppPath}'/>
        </AXUI:func>
    </AXUI:funcs>

OR::

    <AXUI:funcs>
        <AXUI:func name="start_some_element" description="">
            <AXUI:step type="CLI" cmd='{AppPath}'/>
        </AXUI:func>
    </AXUI:funcs>
    
    #in script
    appmap.variables["AppPath"] = "some_app_path"
    
AXUI:includes
-----------------

``AXUI:includes`` can include multiple ``AXUI:include`` elements, ``AXUI:includes`` has no attributes.

AXUI:include
##################

AXUI support include other AppMap to use other AppMap definitions by using ``AXUI:include``, this is used when some app is used by other apps, or you want to extend original app UI elements.

typical usage::

    <AXUI:includes>
        <AXUI:include name="namespace_name" path="included_appmap_name" />
        ...
    </AXUI:includes>
    
    #in script
    appmap.namespace_name.element_name...
    
OR using it as element parent::

    <AXUI:includes>
        <AXUI:include name="namespace_name" path="included_appmap_name" />
        ...
    </AXUI:includes>
    
    <AXUI:UI_elements>
        <AXUI:UI_element name="" parent="namespace_name.element_name" />
    </AXUI:UI_elements>

AXUI:funcs
-----------------

``AXUI:funcs`` can include multiple ``AXUI:func`` element, ``AXUI:funcs`` has no attributes.

AXUI:func
##################

``AXUI:func`` can include multiple ``AXUI:step`` element, ``AXUI:func`` has two attributes "name" and "description".
"name" attribute is to provide an identifier to use this function, this attribute is must have,
"description" provide a description for this function, it's optional.

.. note::

 it's recommend to use ``AXUI:func`` element for UI element start/stop function
 
 not recommend to use ``AXUI:func`` to replace python functions

AXUI:step
""""""""""""""""""

``AXUI:step`` has three attributes: "type", "cmd", "app_map".
"type" specifies step type, could be "CLI" for command or "GUI" for UI operation
"cmd" specifies the detail executing step, for "CLI" type, it's a string of command line; for "GUI" type, it's a string of GUI command just like AXUI command in appmap
"app_map" is optional, indicate which AppMap to execute the step

typical usage::

    <AXUI:funcs>
        <AXUI:func name="wmplayer_start_open_dialog" description="">
            <AXUI:step type="CLI" cmd='"C:\Program Files\Windows Media Player\wmplayer.exe"'/>
            <AXUI:step type="GUI" cmd="wmplayer_Window.keyboard.Input '^o'"/>
            ...
        </AXUI:func>
        ...
    </AXUI:funcs>
    
    <AXUI:UI_elements>
        <AXUI:UI_element name="OpenDialog" parent="" start_func="wmplayer_start_open_dialog"/>
    </AXUI:UI_elements>

AXUI:UI_elements
-----------------

``AXUI:UI_elements`` can include multiple ``AXUI:UI_element`` \\ ``AXUI:Root_element`` \\ ``AXUI:UI_element_group`` elements, ``AXUI:UI_elements`` has no attributes.

AXUI:Root_element
##################

``AXUI:Root_element`` element represents the enter point of UI automation API, like desktop of windows UIA, web browser of ``WebDriver``.

``AXUI:Root_element`` element can include multiple ``AXUI:UI_element`` \\ ``AXUI:UI_element_group`` elements, element included are treated as children of ``AXUI:Root_element`` element.

``AXUI:Root_element`` element has a ``name`` attribute as identifier.

AXUI:UI_element
##################

``AXUI:UI_element`` element represents the normal UI elements,

``AXUI:UI_element`` element can contain multiple ``AXUI:UI_element`` \\ ``AXUI:UI_element_group`` elements, element included are treated as children of ``AXUI:UI_element`` element.

``AXUI:UI_element`` element has six attributes::

- ``name`` attribute, must have, identifier of this element
- ``parent`` attribute, must have for elements of the direct children of ``AXUI:UI_elements``
- ``identifier`` attribute, optional, a string for UI API to find the element, check :ref:`AXUI built-in drivers` for detail identifier format
- ``start_func`` attribute, optional, how to start the element
- ``stop_func`` attribute, optional, how to stop the element
- ``timeout`` attribute, optional, element unique timeout time, will replace global timeout in config file

AXUI:UI_element_group
########################

``AXUI:UI_element_group`` element represents the UI element list,

``AXUI:UI_element_group`` element cannot contain any element,

``AXUI:UI_element_group`` element also has six attributes::

- ``name`` attribute, must have, identifier of this element
- ``parent`` attribute, must have for elements of the direct children of ``AXUI:UI_elements``
- ``identifier`` attribute, optional, a string for UI API to find the element, check :ref:`AXUI built-in drivers` for detail identifier format
- ``start_func`` attribute, optional, how to start the element
- ``stop_func`` attribute, optional, how to stop the element
- ``timedelay`` attribute, optional, will find the element group after time specified
