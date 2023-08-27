from ply import lex, yacc

# Lexer
tokens = (
    'INCLUDE',
    'HEADER',
    'INT',
    'ID',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'RETURN',
)

t_INCLUDE = r'\#include'
t_HEADER = r'<stdio\.h>'
t_INT = r'int'
t_EQUALS = r'='
t_PLUS = r'\+'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RETURN = r'return'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_program(p):
    'program : INCLUDE HEADER INT ID LPAREN RPAREN LBRACE block RETURN NUMBER SEMICOLON RBRACE'
    p[0] = ('program', p[2], p[4], p[8], p[10])

def p_block(p):
    'block : statements'
    p[0] = ('block', p[1])

def p_statements(p):
    'statements : statement statements'
    p[0] = ('statements', p[1], p[2])

def p_statements_empty(p):
    'statements : '
    p[0] = ('statements',)

def p_statement(p):
    'statement : INT ID EQUALS expression SEMICOLON'
    p[0] = ('declare-int', p[2], p[4])

def p_expression(p):
    'expression : term PLUS term'
    p[0] = ('+', p[1], p[3])

def p_term(p):
    'term : ID'
    p[0] = ('ID', p[1])

def p_term_number(p):
    'term : NUMBER'
    p[0] = ('NUMBER', p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Test
data = '''
#include <stdio.h>
int main() {
    int a = 5;
    int b = 10;
    int sum = a + b;
    return 0;
}
'''
result = parser.parse(data, lexer=lexer)
print(result)
