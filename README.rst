
====
AXUI
====

.. image:: https://readthedocs.org/projects/axui/badge/?version=latest
    :target: https://readthedocs.org/projects/axui/?badge=latest
    :alt: Documentation Status

.. image:: https://landscape.io/github/xcgspring/AXUI/master/landscape.svg?style=flat
   :target: https://landscape.io/github/xcgspring/AXUI/master
   :alt: Code Health
    
.. image:: https://img.shields.io/pypi/v/AXUI.svg
    :target: https://pypi.python.org/pypi/AXUI/
    :alt: Latest AXUI version

.. image:: https://img.shields.io/pypi/dm/AXUI.svg
    :target: https://pypi.python.org/pypi/AXUI/
    :alt: Number of PyPI downloads
    
AXUI is short for "Auto eXecute UI", is an UI automation framework, target to minimize the gap between tools and testers.
AXUI provides testers a powerful, unified, easy to use interface for common met platforms, like windows desktop, web, Android, IOS...

AXUI features
==============

1. AXUI provide a plug-in mechanism for automation guy to extend support for different UI
2. AXUI provide built-in drivers for:

    - `windows native UIAutomation Client API <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx>`_ for windows desktop UI
    - `selenium project <https://github.com/SeleniumHQ/selenium>`_ for web UI
    - `appium project <https://github.com/appium/appium>`_ for Android and IOS UI
    
3. AXUI provide an unified, easy to use python interface for use in test scripts
4. AXUI separate UI logic from test scripts, make test scripts more readable and easier to maintain
5. AXUI provide mechanism to handle auto met UI automation issues, like UI response time 

An overview of AXUI structure
=============================

.. image:: http://axui.readthedocs.org/en/latest/_images/AXUI_structure.PNG
    :target: http://axui.readthedocs.org/en/latest/_images/AXUI_structure.PNG
    :alt: AXUI structure

code demonstrations
==============================

This code is in ``example/selenium``, it's a simple example to demonstrate how AXUI separate UI logic from test script.

Though this example give us a impression that AXUI add extra complexities but doesn't improve code readability.
Image that an app contains a lot of UI Elements, and the search identifiers split into multiple test scripts, then AXUI can gather all UI identifiers into one appmap, and make your scripts clean to read and maintain.

*Original*::

    import selenium.webdriver as webdriver

    browser = webdriver.Chrome(executable_path = r"chromedriver.exe")
    browser.get(r"http://www.bing.com")

    searchEdit = browser.find_element_by_id("sb_form_q")
    goButton = browser.find_element_by_id("sb_form_go")

    searchEdit.send_keys("AXUI")
    goButton.click()

*AXUI AppMap*::

    <AXUI:app_map xmlns:AXUI="AXUI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="AXUI AXUI_app_map.xsd">
        <AXUI:funcs>
            <AXUI:func name="go_to_bing" description="">
                <AXUI:step type="GUI" cmd='browser.BrowserPattern.get "http://www.bing.com"'/>
            </AXUI:func>
        </AXUI:funcs>

        <AXUI:UI_elements>
            <AXUI:Root_element name="browser" >
                <AXUI:UI_element name="searchEdit" identifier="id='sb_form_q'" start_func="go_to_bing"/>
                <AXUI:UI_element name="goButton" identifier="id='sb_form_go'" start_func="go_to_bing"/>
            </AXUI:Root_element>
        </AXUI:UI_elements>
    </AXUI:app_map>

*AXUI Code*::

    import AXUI

    config_file = "selenium.cfg"
    app_map = "www.bing.com.xml"

    AXUI.Config(config_file)
    appmap = AXUI.AppMap(app_map)

    appmap.browser.start(browser_name="CHROME", executable_path = r"chromedriver.exe")

    appmap.browser.searchEdit.Keyboard.input("AXUI")
    appmap.browser.goButton.Mouse.left_click()


More details, please check `AXUI documents <http://axui.readthedocs.org/en/latest/index.html>`_

To have quick experience about AXUI, please check `AXUI samples <http://axui.readthedocs.org/en/latest/Appendices.html#samples>`_
