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

ToDo list
==========================

- Multiple languages support, to support internationalization test

