
import sys
import unittest

class FakeUIElement(object):
    def SetFocus(self):
        pass
        
    def GetClickablePoint(self):
        return 600, 300


class TestUIA(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_keyboard(self):
        from AXUI.driver.windows.win32 import Keyboard
        keyboard = Keyboard(FakeUIElement())
        keyboard.Input("~d")

        
