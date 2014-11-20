
import os
import unittest

import AXUI.config as config_module
import fake_module

class TestConfig(unittest.TestCase):
    
    def test_config_self(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_module.config_self(os.path.join(current_dir, "test.config"))
    
    def test_config_module(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_module.config_self(os.path.join(current_dir, "test.config"))
        configs = config_module.config(fake_module)
        self.assertEqual(configs["config1"], "test1")
        self.assertEqual(configs["config2"], "test2")
        self.assertEqual(configs["config3"], "test3")
