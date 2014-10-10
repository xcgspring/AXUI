'''
In app map, sometimes need to describe how to start and close one UI element
So create a simple command language to satify this.
this language is like:
'elementX.elementY.operation [parameter1 parameter2 ...]'
parameter could be number,string,bool,list,tuple
'''

import ply.lex as lex
import ply.yacc as yacc

import AXUI.logger as AXUI_logger

LOGGER = AXUI_logger.get_logger()

##################################
#lexical analysis
##################################

tokens = ("PERIOD", "TERM", "NUMBER", "STRING", "BOOL", "LIST", "TUPLE")

#ignore characters
t_ignore = ' \t\x0c'

#newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_PERIOD = r"\."

def t_TERM(t):
    r'[\w_]'
    return t
    
def t_NUMBER(t):
    r'\d+'
    return t
    
def t_STRING(t):
    '(\"(.)*?\")|(\'(.)*?\')' 
    return t

def t_LIST(t):
    




