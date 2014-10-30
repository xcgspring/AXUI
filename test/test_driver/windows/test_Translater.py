
import sys
import unittest

class TestUIA(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_app_map_create(self):
        import AXUI.driver.windows.UIA as UIA



