'''
In app map, sometimes need to describe how to start and close one UI element
So create a simple command language to satify this.
this language is like:
'elementX.elementY.operation [parameter1 parameter2 ...]'
parameter could be number,string,bool,list,tuple
this module will parse command to a list like:
([elementX, elementY, operation], [parameter1, parameter2, ...])
'''

#TODO
#1. Fix p.lineno not correct issue

import ply.lex as lex
import ply.yacc as yacc

from AXUI.logger import LOGGER

##################################
#lexical analysis
##################################

tokens = ("PERIOD", "COMMA", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "OBJECT", "NUMBER", "STRING", "BOOL")

#ignore characters
t_ignore = ' \t\x0c'

#newline
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_PERIOD = r"\."
t_COMMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"

def t_NUMBER(t):
    r'\d+'
    return t

def t_OBJECT(t):
    r'[\w_]+'
    if t.value.upper() in ("TRUE", "FALSE"):
        t.type = "BOOL"
    return t
    
def t_STRING(t):
    '(\"(.)*?\")|(\'(.)*?\')' 
    return t

def t_error(t):
    LOGGER().debug("Illegal character %s in Ln: %d" % (repr(t.value[0]), t.lexer.lineno))
    t.lexer.skip(1)

gui_command_lexer = lex.lex()

##################################
#Syntactic analysis
##################################
def p_operation_1(p):
    "operation : object_list parameter_list"
    p[0] = (p[1], p[2])

def p_operation_2(p):
    "operation : object_list"
    p[0] = (p[1], [])

def p_object_list_1(p):
    "object_list : OBJECT"
    p[0] = [p[1]]

def p_object_list_2(p):
    "object_list : object_list PERIOD OBJECT"
    p[0] = p[1]
    p[0].append(p[3])
    
    
def p_parameter_list_1(p):
    "parameter_list : parameter"
    p[0] = [p[1]]
    
def p_parameter_list_2(p):
    "parameter_list : parameter_list parameter"
    p[0] = p[1]
    p[0].append(p[2])
    
def p_parameter(p):
    '''parameter : member'''
    p[0] = p[1]

def p_list(p):
    "list : LBRACKET members RBRACKET"
    p[0] = p[2]
    
def p_tuple(p):
    "tuple : LPAREN members RPAREN"
    p[0] = tuple(p[2])
    
def p_members_1(p):
    "members : member"
    p[0] = [p[1]]
    
def p_members_2(p):
    "members : members COMMA member"
    p[0] = p[1]
    p[0].append(p[3])
    
def p_member(p):
    '''member : number
              | string
              | BOOL
              | list
              | tuple'''
    p[0] = p[1]

def p_string(p):
    "string : STRING"
    p[0] = p[1].strip("\"").strip("\'")
    
def p_number(p):
    "number : NUMBER"
    p[0] = int(p[1])
              
def p_error(p):
    LOGGER().debug("Syntax error in input: %s, Ln: %d" % (repr(p.value), p.lineno))

gui_command_parser = yacc.yacc(write_tables=0)

