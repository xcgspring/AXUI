
import sys
import unittest

class TestUIA(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_root(self):
        import AXUI.driver.windows.UIElement as UIElement
        root_element = UIElement.get_root()
        self.assertIsNotNone(root_element)



