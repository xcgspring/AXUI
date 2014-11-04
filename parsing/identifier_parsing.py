'''
this module is used to parse identifier descriptions, based on python ply library
identifier description is like:
'name="xxx" AND class="yyy" OR ((ID = 12312 And enabled="no") AND index=2)'
this module will parse this identifier to a list like:
("OR", ("AND", (name, "xxx"), (class, "yyy")), ("AND", ("AND", (ID, 12312), (enabled, "no")), (index, 2))
'''

#TODO
#1. Fix p.lineno not correct issue

import ply.lex as lex
import ply.yacc as yacc

import AXUI.logger as AXUI_logger

LOGGER = AXUI_logger.get_logger()

##################################
#lexical analysis
##################################
reserved = ("AND", "OR")
tokens = reserved+("EQUALS", "LPAREN", "RPAREN", "TERM", "STRING", "NUMBER", "BOOL")

#ignore characters
t_ignore = ' \t\x0c'

#newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    return t
    
def t_TERM(t):
    r'[\w_]+'
    if t.value.upper() in reserved:
        t.type = t.value.upper()
    elif t.value.upper() in ("TRUE", "FALSE"):
        t.type = "BOOL"
    else:
        t.type = "TERM"
    return t
    
def t_STRING(t):
    '(\"(.)*?\")|(\'(.)*?\')' 
    return t
    
def t_error(t):
    LOGGER.warn("Illegal character %s in Ln: %d" % (repr(t.value[0]), t.lexer.lineno))
    raise Exception("")
    t.lexer.skip(1)
    
identifier_lexer = lex.lex()

##################################
#Syntactic analysis
##################################
def p_identifier_and(p):
    'identifier : identifier AND identifier'
    p[0]=("AND", p[1], p[3])
    
def p_identifier_or(p):
    'identifier : identifier OR identifier'
    p[0]=("OR", p[1], p[3])
    
def p_identifier_paren(p):
    'identifier : LPAREN identifier RPAREN'
    p[0]=p[2]
    
def p_identifier(p):
    'identifier : TERM EQUALS value'
    p[0]=(p[1], p[3])
    
def p_value_number(p):
    'value : NUMBER'
    p[0]=p[1]
    
def p_value_string(p):
    'value : STRING'
    p[0]=p[1].strip("\"").strip("\'")
    
def p_value_bool(p):
    'value : BOOL'
    p[0]=p[1]
    
def p_error(p):
    LOGGER.warn("Syntax error in input: %s, Ln: %d" % (repr(p.value), p.lineno))
    raise Exception("")
    
identifier_parser = yacc.yacc(write_tables=0)
