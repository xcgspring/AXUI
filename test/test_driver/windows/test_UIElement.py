
import sys
import unittest

class TestUIA(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_root(self):
        import AXUI.driver.windows.UIElement as UIElement
        root_element = UIElement.get_root()
        print root_element
        self.assertIsNotNone(root_element)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_wmplayer(self):
        import AXUI.driver.windows.UIElement as UIElement
        root_element = UIElement.get_root()
        import subprocess
        subprocess.Popen("\"C:\\Program Files\\Windows Media Player\\wmplayer.exe\"")
        from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
        identifier = "Name='Windows Media Player'"
        parsed_identifier = identifier_parser.parse(identifier, lexer=identifier_lexer)
        print parsed_identifier
        wmplayer_window = root_element.find(parsed_identifier)
        print wmplayer_window
