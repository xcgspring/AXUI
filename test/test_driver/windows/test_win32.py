
import sys
import unittest

class FakeUIElement(object):
    def SetFocus(self):
        pass
        
    def GetClickablePoint(self):
        return 600, 300


class TestWin32(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_keyboard(self):
        from AXUI.driver.windows.win32 import Keyboard
        keyboard = Keyboard(FakeUIElement())
        keyboard.Input("~d")
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_mouse(self):
        from AXUI.driver.windows.win32 import Mouse
        mouse = Mouse(FakeUIElement())
        print(mouse)
        mouse.RightClick()

        
