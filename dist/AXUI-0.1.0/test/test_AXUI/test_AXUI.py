
import unittest

class TestAXUI(unittest.TestCase):

    def test_Config(self):
        import os
        import AXUI
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "test.cfg")
        AXUI.Config(config_file)
        
    def test_AppMap(self):
        import AXUI
        pass
