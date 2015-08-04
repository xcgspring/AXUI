import logging

def config_logger():
    logger = logging.getLogger(logger_config.logger_name)
    logger.propagate = False
    logger.setLevel(logger_config.logging_level)
    logger.handlers = []

    file_handler = logging.FileHandler(logger_config.logging_file_name, mode="w")
    file_handler.setLevel(logger_config.logging_level)
    formatter = logging.Formatter(logger_config.logging_formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

class Config(object):

    _logger_name = "AXUI"
    _logging_level = logging.DEBUG
    _logging_file_name = "AXUI.log"
    _logging_formatter = "[ %(levelname)s ][ %(filename)s:%(lineno)d ] %(message)s"

    def __str__(self):
        return ""

    @property
    def logger_name(self):
        return self._logger_name

    @logger_name.setter
    def logger_name(self, input):
        self._logger_name = str(input)
        config_logger()

    @property
    def logging_level(self):
        return self._logging_level

    @logging_level.setter
    def logging_level(self, input):
        logging_levels = {"CRITICAL":logging.CRITICAL,
                          "ERROR":logging.ERROR,
                          "WARNING": logging.WARN,
                          "WARN": logging.WARN,
                          "INFO": logging.INFO,
                          "DEBUG": logging.DEBUG
                          logging.CRITICAL: logging.CRITICAL,
                          logging.ERROR: logging.ERROR,
                          logging.WARN: logging.WARN,
                          logging.INFO: logging.INFO,
                          logging.DEBUG: logging.DEBUG,}

        if input in logging_levels:
            self._logging_level = logging_levels[input]
        elif isinstance(input, str) and input.upper() in logging_levels:
            self._logging_level = logging_levels[input.upper()]
        else:
            raise ValueError("Invalid logging level %s" % input)
        config_logger()

    @property
    def logging_file_name(self):
        return self._logging_file_name

    @logging_file_name.setter
    def logging_file_name(self, input):
        self._logging_file_name = str(input)
        config_logger()

    @property
    def logging_formatter(self):
        return self._logging_formatter

    @logging_formatter.setter
    def logging_formatter(self, input):
        self._logging_formatter = str(input)
        config_logger()

logger_config = Config()