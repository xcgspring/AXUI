# lextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'AND': 1, 'TERM': 1, 'RPAREN': 1, 'STRING': 1, 'EQUALS': 1, 'NUMBER': 1, 'BOOL': 1, 'LPAREN': 1, 'OR': 1}
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NEWLINE>\\n+)|(?P<t_NUMBER>\\d+)|(?P<t_TERM>[\\w_]+)|(?P<t_STRING>"(.)*?")|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_EQUALS>=)', [None, ('t_NEWLINE', 'NEWLINE'), ('t_NUMBER', 'NUMBER'), ('t_TERM', 'TERM'), ('t_STRING', 'STRING'), None, (None, 'LPAREN'), (None, 'RPAREN'), (None, 'EQUALS')])]}
_lexstateignore = {'INITIAL': ' \\t\\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
