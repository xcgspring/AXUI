#TODO
#1. Add comments and tests

import sys
import logging
import color
import platform

__all__=[config_logger, default_configs, LOGGER]

LOGNAME = None
LOGGER = get_logger()

default_configs = {"logger_name":"AXUI", 
                   "logging_level":"DEBUG", 
                   "logging_stream":"stdout", 
                   "logging_file":"", 
                   "file_logging_mode":"a", 
                   "formatter":"%(message)%", 
                   "color":"True" }
                   
logging_levels = {"CRITICAL":logging.CRITICAL, 
                  "ERROR":logging.ERROR, 
                  "WARNING": logging.WARNING, 
                  "INFO": logging.INFO, 
                  "DEBUG": logging.DEBUG, 
                  "NOTSET": logging.NOTSET }
                  
logging_stream = {"STDOUT":sys.stdout, 
                 "FALSE":False }
                 
file_logging_mode = {"A":"a", 
                     "W":"w" }
                 
logging_color = {"TRUE":True, 
                 "FALSE":False }
                 
def config_logger(configs=default_configs):
    '''
    '''
    #verify input configs
    if not configs["logger_name"]:
        configs["logger_name"]=default_configs["logger_name"]
    
    if configs["logging_levels"].upper() in logging_levels:
        configs["logging_levels"]=logging_levels[configs["logging_levels"].upper()]
    else:
        configs["logging_levels"]=logging_levels[default_configs["logging_levels"]]
        
    if configs["logging_stream"].upper() in logging_stream:
        configs["logging_stream"]=logging_stream[configs["logging_stream"]]
    else:
        configs["logging_stream"]=logging_stream[default_configs["logging_stream"]]
        
    if configs["file_logging_mode"].upper() in file_logging_mode:
        configs["file_logging_mode"]=file_logging_mode[configs["file_logging_mode"].upper()]
    else:
        configs["file_logging_mode"]=logging_levels[default_configs["file_logging_mode"]]
        
    if not configs["formatter"]:
        configs["formatter"]=default_configs["formatter"]
        
    if configs["color"].upper() in logging_color:
        configs["color"]=logging_color[configs["color"].upper()]
    else:
        configs["color"]=logging_color[default_configs["color"]]
        
    #config logger according input configs
    logger = logging.getLogger(configs["logger_name"])
    logger.propagate = False
    logger.setLevel(configs["logging_level"])

    if configs["logging_stream"]:
        stream_handler = logging.StreamHandler(configs["logging_stream"])
        stream_handler.setLevel(configs["logging_level"])

        formatter = logging.Formatter(configs["formatter"])
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        
    if configs["logging_file"]:
        file_handler = logging.FileHandler(configs["logging_file"], mode=configs["file_logging_mode"])
        file_handler.setLevel(configs["logging_level"])

        formatter = logging.Formatter(configs["formatter"])
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
    
    if color:
        if platform.system()=='Windows':
            # Windows does not support ANSI escapes 
            # and we are using API calls to set the console color
            logging.StreamHandler.emit = \
            color.add_coloring_to_emit_windows(logging.StreamHandler.emit)
        else:
            # all non-Windows platforms are supporting ANSI escapes so we use them
            logging.StreamHandler.emit = \
            color.add_coloring_to_emit_ansi(logging.StreamHandler.emit)

    LOGNAME = configs["logger_name"]
    
def get_logger():
    if LOGNAME == None:
        raise NotImplementedError("Logger not configure yet")
    else:
        return logging.getLogger(LOGNAME)

