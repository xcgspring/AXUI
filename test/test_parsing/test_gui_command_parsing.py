
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.command = '''x.y.asfas 'asf' 123 'true' true ('asdf', ('asdf', 12))'''
        
    def test_lex(self):
        from AXUI.parsing.gui_command_parsing import gui_command_lexer

        gui_command_lexer.input(self.command)
        while True:
            tok = gui_command_lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.gui_command_parsing import gui_command_lexer, gui_command_parser
        print gui_command_parser.parse(self.command, lexer=gui_command_lexer)

if __name__=="__main__":
    unittest.main(verbosity=2)

