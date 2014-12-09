#TODO
#1. Add comments and tests

import sys
import logging
import platform

import _color

LOGNAME = None

config_section = "logging"

default_configs = {"logger_name":"AXUI", 
                   "logging_level_file":"DEBUG",
                   "logging_level_stream":"ERROR", 
                   "logging_stream":"stdout", 
                   "logging_file":"AXUI.log", 
                   "file_logging_mode":"a", 
                   "formatter":"[ %(levelname)s ][ %(filename)s:%(lineno)d ] %(message)s", 
                   "color_enable":"True" }
                   
logging_levels = {"CRITICAL":logging.CRITICAL, 
                  "ERROR":logging.ERROR, 
                  "WARNING": logging.WARNING, 
                  "INFO": logging.INFO, 
                  "DEBUG": logging.DEBUG}
                  
logging_streams = {"STDOUT":sys.stdout, 
                 "FALSE":False }
                 
file_logging_modes = {"A":"a", 
                     "W":"w" }
                 
logging_color_configs = {"TRUE":True, 
                 "FALSE":False }
                 
def config(configs=default_configs):
    '''config logger with settings in configure file
    '''
    logger_name=configs["logger_name"]
    
    if configs["logging_level_file"].upper() in logging_levels:
        logging_level_file=logging_levels[configs["logging_level_file"].upper()]
    else:
        #print("Error logging_level_file value, use default")
        logging_level_file=logging_levels[default_configs["logging_level_file"].upper()]
        
    if configs["logging_level_stream"].upper() in logging_levels:
        logging_level_stream=logging_levels[configs["logging_level_stream"].upper()]
    else:
        #print("Error logging_level_stream value, use default")
        logging_level_stream=logging_levels[default_configs["logging_level_stream"].upper()]
        
    if configs["logging_stream"].upper() in logging_streams:
        logging_stream=logging_streams[configs["logging_stream"].upper()]
    else:
        #print("Error logging_stream value, use default")
        logging_stream=logging_streams[default_configs["logging_stream"].upper()]
        
    if configs["file_logging_mode"].upper() in file_logging_modes:
        file_logging_mode=file_logging_modes[configs["file_logging_mode"].upper()]
    else:
        #print("Error file_logging_mode value, use default")
        file_logging_mode=file_logging_modes[default_configs["file_logging_mode"].upper()]
        
    formatter_string=configs["formatter"]
    
    if configs["color_enable"].upper() in logging_color_configs:
        logging_color_config=logging_color_configs[configs["color_enable"].upper()]
    else:
        #print("Error color_enable value, use default")
        logging_color_config=logging_color_configs[default_configs["color_enable"].upper()]
        
    #config logger according input configs
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    logger.handlers = []

    if logging_stream:
        stream_handler = logging.StreamHandler(logging_stream)
        stream_handler.setLevel(logging_level_stream)
        formatter = logging.Formatter(formatter_string)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        
    file_handler = logging.FileHandler(configs["logging_file"], mode=file_logging_mode)
    file_handler.setLevel(logging_level_file)
    formatter = logging.Formatter(formatter_string)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    if logging_color_config:
        if platform.system()=='Windows':
            # Windows does not support ANSI escapes 
            # and we are using API calls to set the console color
            logging.StreamHandler.emit = \
            _color.add_coloring_to_emit_windows(logging.StreamHandler.emit)
        else:
            # all non-Windows platforms are supporting ANSI escapes so we use them
            logging.StreamHandler.emit = \
            _color.add_coloring_to_emit_ansi(logging.StreamHandler.emit)

    global LOGNAME
    LOGNAME = logger_name

#used by config module
__all__=["config_section", "default_configs", "config"]

def LOGGER():
    global LOGNAME
    if LOGNAME == None:
        config()
    return logging.getLogger(LOGNAME)

    
