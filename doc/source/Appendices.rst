.. _`Appendices`:

=========================
Appendices
=========================

:Page Status: Development
:Last Reviewed: 

Samples
===========================

sample codes in ``AXUI/example``, here I give a step by step guide how to launch the examples

windows
-----------------------

My test environment is win8.1 64bit, anyway win8.1 32bit machine is OK. For win7/win8, you may need to change the AppMap, since UI changes for different windows version.

Prepare Environment
##########################

1. Install `python 2.7 <https://www.python.org>`_
2. Install setuptools + pip. check `python package management <http://use-python.readthedocs.org/zh_CN/latest/package_management.html>`_
3. Install `comtypes <https://pypi.python.org/pypi/comtypes>`_
4. Install AXUI 
5. Config windows path, add python path (usually ``c:\python27``) to windows path

Run the example in ``example/windows``
############################################

1. Modify the config file, check :ref:`config AXUI`
2. Run the script, ``python wmplayer_wrapper.py``

selenium webdriver
-----------------------

My test environment is win8.1 64bit, with chrome browser. Other environment supported by selenium should also be OK.

Prepare Environment 
##########################

1. Install `python 2.7 <https://www.python.org>`_
2. Install setuptools + pip. check `python package management <http://use-python.readthedocs.org/zh_CN/latest/package_management.html>`_
3. Install `selenium <https://pypi.python.org/pypi/selenium/2.45.0>`_
4. Install AXUI 
5. Config windows path, add python path (usually ``c:\python27``) to windows path

Run the example in ``example/selenium``
#############################################

1. Modify the config file, check :ref:`config AXUI`
2. Run the script, ``python bing.py``

appium webdriver
-----------------------

Prepare Environment 
##########################

My test environment is win7 64bit, here is my steps to prepare appium environment.

1. Install appium, two methods for windows

 1. Install node.js
 2. Install appium, ``npm install -g appium``
 
 OR
 
 1. Download and install AppiumForWindow from `github <https://github.com/appium/appium/releases>`_
 
2. Prepare Android develop environment, include SDK and AVD. Check `this website <http://www.androiddevtools.cn/>`_ for available mirrors for china
3. Install `selenium <https://pypi.python.org/pypi/selenium/2.45.0>`_
4. Install `Appium-Python-Client <https://pypi.python.org/pypi/Appium-Python-Client>`_
5. Install AXUI

Run the example in ``example/appium``
#############################################

1. Launch appium server, you need set the Android SDK path for appium server, should not contain white space.
2. Modify the config file, check :ref:`config AXUI`
3. Run the script, ``python simple.py``, this sample is modified from `appium sample code <https://github.com/appium/sample-code/blob/master/sample-code/examples/python/android_simple.py>`_
4. Check the AVD is act as expected

ToDo list
==========================

- Multiple languages support, to support internationalization test
- Define an unified interfaces for different driver UI actions
- Support for python 3