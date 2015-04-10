.. _`config AXUI`:

=========================
AXUI configurations
=========================

:Page Status: Development
:Last Reviewed: 

AXUI configurations overview
=============================

AXUI support some custom configurations, to make AXUI suite your test environment.
AXUI use a config file to specify these configurations, config format is compatible with `RFC 822 <http://tools.ietf.org/html/rfc822.html>`_,
so that we can parse it with python built-in `ConfigParser <https://docs.python.org/2/library/configparser.html>`_ module

Below is the default configuration file in ``AXUI/global.cfg``::

    [logging]
    #logger name
    logger_name = AXUI

    #logging level
    #valid levels are DEBUG,INFO,WARNING,ERROR,CRITICAL
    logging_level_file = DEBUG
    logging_level_stream = ERROR

    #logging file name
    logging_file = AXUI.log

    #logging file mode
    #"w" for overwrite, will create a new file
    #"a" for append, will append the log if there is an existing file
    file_logging_mode = a

    #logging format
    #please check https://docs.python.org/2/library/logging.html#logrecord-attributes
    #for more available formats
    formatter = %(message)s

    #if enable colorful logging, "True" or "False"
    color_enable = True
        
    [XML]
    #location where you store your app maps, should be an absolute path
    #set this location wrong could cause your app map loading fail
    app_map_location = abspath

    #location where you store your schema, should be an absolute path
    #usually you do not need to change the default schema
    #so do not set this unless you know what your are doing
    #schema_location = abspath

    #global timeout for UI response
    time_out = 5

    #screenshot file location
    #need abspath
    screenshot_location = abspath

    #enable screenshot when fail happens
    #can only set to True or False, other value will be ignore
    screenshot_on_failure = False

    [image]
    #if generate diff image
    #can only set to True or False, other value will be ignore
    gen_diff_image = True

    #diff image location
    #need abspath
    diff_image_location = abspath

    [driver]
    #driver used in your UI automation
    driver_used = windows


AXUI configuration sections
=============================

Just introduce some common used configure settings

logging
---------

- logger_name: you can change logger_name to keep consistent with your app
- logging_file: AXUI log file, you can specify a abs path or relative path

XML
---------

- app_map_location: you need to set your app map location, make sure AXUI can find an app map file has same name as your specified
- schema_location: default is ``AXUI/XML/schema``, you usually do not need to change it
- time_out: global timeout for UI response, you can set it bigger for slow machine/website
- screenshot_on_failure: set this true will turn on screen shot when UI operation fails

image
---------

- gen_diff_image: set this to true will generate diff image for image compare

driver
----------

- driver_used: your driver module name used currently, like "windows" for windows driver

