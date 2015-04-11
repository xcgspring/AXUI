.. _`AXUI built-in drivers`:

=========================
AXUI built-in drivers
=========================

:Page Status: Development
:Last Reviewed: 

AXUI has implement some drivers for common used platforms

- windows desktop, based on `windows native UIAutomation Client API <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684021(v=vs.85).aspx>`_
- web, based on `selenium project <https://github.com/SeleniumHQ/selenium>`_
- mobile android/ios, based on `appium project <https://github.com/appium/appium>`_

driver for windows UIAutomation API
====================================

driver for windows UIAutomation API is in ``driver/windows``, we use `comtypes <https://github.com/enthought/comtypes>`_ to access this windows COM API, 
thus to use AXUI to automate windows UI, you need install `comtypes <https://github.com/enthought/comtypes>`_ first.

Windows UIAutomation API separates operations for different kinds of UI into a set of `control patterns <https://msdn.microsoft.com/en-us/library/windows/desktop/ee684023(v=vs.85).aspx>`_, 
it's recommended to use these patterns to operate target UI,
AXUI expose these patterns to end users, anyway end users should need to have a check of these patterns.

.. note::

 I have tested windows driver on win8.1 and win10,
 
 - it's works well with windows UI framework like win32, winform, WPF, windows store app
 - not works well with Qt framework, UIA recognize all kinds of Qt controls as frames  
 - not support for directX, custom UI controls

How to use identifier to search element
----------------------------------------


.. note::

 inspect tool

UIA element properties
----------------------


UIA element patterns
----------------------



driver for `WebDriver <https://w3c.github.io/webdriver/webdriver-spec.html>`_ compatible projects
===================================================================================================

``selenium`` and ``appium`` all use a C/S structure to support multiple languages, the client side and server side use `WebDriver <https://w3c.github.io/webdriver/webdriver-spec.html>`_ protocol to communicate with each other.
since ``selenium`` and ``appium`` already have python clients, we don't reinvent the wheel, but use these python clients to implement our drivers for AXUI

selenium
-----------------



.. note::

 Only have some tests with IE with selenium driver 

appium
-----------------


.. note::

 since I don't have an apple/android environment, the appium driver is not tested
 
 I will be very glad someone can have a test for it :)