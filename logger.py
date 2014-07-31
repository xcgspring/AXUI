import sys
import logging
import color
import platform

__all__=[configure_logger, get_logger]

if platform.system()=='Windows':
    # Windows does not support ANSI escapes 
    # and we are using API calls to set the console color
    logging.StreamHandler.emit = \
    color.add_coloring_to_emit_windows(logging.StreamHandler.emit)
else:
    # all non-Windows platforms are supporting ANSI escapes so we use them
    logging.StreamHandler.emit = \
    color.add_coloring_to_emit_ansi(logging.StreamHandler.emit)

LOGNAME = None

def configure_logger(name="AXUI", stream=sys.stdout, level=logging.DEBUG, formatter="%(message)%"):
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)

    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(level)

    formatter = logging.Formatter(formatter)
    streamHandler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    LOGNAME = name
    
def get_logger():
    if loggerName == None:
        raise NotImplementedError("Need configureLogger before use getLogger")
    else:
        return logging.getLogger(loggerName)

