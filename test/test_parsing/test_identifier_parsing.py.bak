
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.identifier = 'Name=\'xxx\' and class = "yyy" or ((id = 123 and index = 1) and enabled = tRUE)'

    def test_lex(self):
        from AXUI.parsing.identifier_parsing import identifier_lexer

        identifier_lexer.input(self.identifier)
        while True:
            tok = identifier_lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.identifier_parsing import identifier_lexer, identifier_parser
        print identifier_parser.parse(self.identifier, lexer=identifier_lexer)

