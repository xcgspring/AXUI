'''
Parsing for CLI string
CLI string is like:
'executer parameter1 parameter2 ...'
this module will parse command to a list like:
([executer, parameter1, parameter2, ...])
executer or parameter surround by '{}' will be replaced by variables
'''

#TODO
#1. Fix p.lineno not correct issue

import ply.lex as lex
import ply.yacc as yacc

from AXUI.logger import LOGGER

##################################
#lexical analysis
##################################

tokens = ("LBRACE", "RBRACE", "DQUOTA", "SQUOTA", "OBJECT")

#ignore characters
t_ignore = ' \t\x0c'

#newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_LBRACE = r"{"
t_RBRACE = r"}"
t_DQUOTA = r"\""
t_SQUOTA = r"'"

def t_OBJECT(t):
    r'[\w\W]+'
    return t

def t_error(t):
    LOGGER().debug("Illegal character %s in Ln: %d" % (repr(t.value[0]), t.lexer.lineno))
    t.lexer.skip(1)

command_lexer = lex.lex()

##################################
#Syntactic analysis
##################################    

def p_objects(p):
    "objects : objects variable"
    p[1].append(p[2])
    p[0] = p[1]

def p_variable(p):
    "variable : LBRACE objects RBRACE"
    p[0] = "{"+" ".join(p[2])+"}"

def p_objects(p):
    "objects : SQUOTA objects SQUOTA"
    p[0] = [" ".join(p[2])]

def p_objects(p):
    "objects : DQUOTA objects DQUOTA"
    p[0] = [" ".join(p[2])] 
    
def p_objects(p):
    "objects : objects OBJECT"
    p[1].append(p[2])
    P[0] = p[1]
    
def p_objects(p):
    "objects : OBJECT"
    p[0] = [p[1]]
              
def p_error(p):
    LOGGER().debug("Syntax error in input: %s, Ln: %d" % (repr(p.value), p.lineno))

command_parser = yacc.yacc(write_tables=0)

