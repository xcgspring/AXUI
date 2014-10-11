
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.command = r"x.y.asfas 'asf' 123 'true' true ('asdf', ('asdf', 12))"
        
    def test_lex(self):
        from AXUI.parsing.identifier_parsing import lexer

        lexer.input(self.command)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.identifier_parsing import parser
        print parser.parse(self.command)

