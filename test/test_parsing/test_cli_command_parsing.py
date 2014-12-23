
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.command = r'''"c:\test\test 1\1.exe" {variable} parameter2 parameter3'''
        
    def test_lex(self):
        from AXUI.parsing.cli_command_parsing import cli_command_lexer

        cli_command_lexer.input(self.command)
        while True:
            tok = cli_command_lexer.token()
            if not tok:
                break
            print tok
        
    def test_yacc(self):
        from AXUI.parsing.cli_command_parsing import cli_command_lexer, cli_command_parser
        print cli_command_parser.parse(self.command, lexer=cli_command_lexer)

if __name__=="__main__":
    unittest.main(verbosity=2)

