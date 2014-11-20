
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.command = '''x.y.asfas 'asf' 123 'true' true ('asdf', ('asdf', 12))'''
        
    def test_lex(self):
        from AXUI.parsing.command_parsing import command_lexer

        command_lexer.input(self.command)
        while True:
            tok = command_lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.command_parsing import command_lexer, command_parser
        print command_parser.parse(self.command, lexer=command_lexer)

if __name__=="__main__":
    unittest.main(verbosity=2)

