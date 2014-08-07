
import unittest

class TestConfigLogger(unittest.TestCase):
    def setUp(self):
        import AXUI.logger
        self.AXUI_logger = AXUI.logger
        
    def test_valid_config(self):
        valid_configs = {"logger_name":"TestConfigLogger", 
                   "logging_level":"DEBUG", 
                   "logging_stream":"stdout", 
                   "logging_file":"test_config_logger.log", 
                   "file_logging_mode":"a", 
                   "formatter":"%(message)%", 
                   "color":"True" }
                   
        self.AXUI_logger.config_logger(valid_configs)
        logger = self.AXUI_logger.get_logger()
        self.assertTrue(logger)
        self.assertEqual(logger.name, "TestConfigLogger")
        
    def tearDown(self):
        pass
        
class TestLogger(unittest.TestCase):
    def setUp(self):
        import AXUI.logger
        self.AXUI_logger = AXUI.logger
        valid_configs = {"logger_name":"TestLogger", 
                   "logging_level":"DEBUG", 
                   "logging_stream":"stdout", 
                   "logging_file":"test_logger.log", 
                   "file_logging_mode":"a", 
                   "formatter":"%(message)%", 
                   "color":"True" }
                   
        self.AXUI_logger.config_logger(valid_configs)
        self.logger = self.AXUI_logger.get_logger()
        
    def test_logger(self):
        self.logger.debug("test debug")
        self.logger.info("test info")
        self.logger.warn("test warn")
        self.logger.error("test error")
        self.logger.critical("test critical")
        
    def tearDown(self):
        pass
        
        
