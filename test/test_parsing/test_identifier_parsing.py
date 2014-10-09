
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.identifier = 'name="xxx" and class = "yyy" or ((id = 123 and index = 1) and enabled = tRUE)'
        
    def test_lex(self):
        from AXUI.parsing.identifier_parsing import lexer

        lexer.input(self.identifier)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.identifier_parsing import parser
        print parser.parse(self.identifier)

