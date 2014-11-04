
import sys
import unittest

class TestUIA(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_UIA_wrapper(self):
        import AXUI.driver.windows.UIA as UIA
        self.assertTrue(UIA.UIA_wrapper)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_IUIAutomation_object(self):
        import AXUI.driver.windows.UIA as UIA
        self.assertTrue(UIA.IUIAutomation_object)
        
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_UIA_enums(self):
        import AXUI.driver.windows.UIA as UIA
        self.assertIsNotNone(UIA.UIA_enums["WindowVisualState"]["WindowVisualState_Maximized"])
        
        
