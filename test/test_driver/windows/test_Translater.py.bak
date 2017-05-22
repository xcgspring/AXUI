
import sys
import unittest

class TestTranslater(unittest.TestCase):            
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_coordinate_identifier(self):
        import AXUI.driver.windows.Translater as translater
        from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
        identifier = "Coordinate = '(12 ,34, 56, 79)'"
        parsed_identifier = identifier_parser.parse(identifier, lexer=identifier_lexer)
        translated_identifier = translater.ID_Translater(parsed_identifier).get_translated()
        print translated_identifier
        
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_index_identifier(self):
        import AXUI.driver.windows.Translater as translater
        from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
        identifier = "Name='menu bar' AND Index=3"
        parsed_identifier = identifier_parser.parse(identifier, lexer=identifier_lexer)
        translated_identifier = translater.ID_Translater(parsed_identifier).get_translated()
        print translated_identifier

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_UIA_identifier(self):
        import AXUI.driver.windows.Translater as translater
        from  AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser 
        identifier = "Name='menu bar' AND LocalizedControlType='menu bar'"
        parsed_identifier = identifier_parser.parse(identifier, lexer=identifier_lexer)
        translated_identifier = translater.ID_Translater(parsed_identifier).get_translated()
        print translated_identifier
        
