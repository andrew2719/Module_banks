from ply import lex, yacc

# Lexer
tokens = (
    'NUMBER',
    'PLUS',
    'SEMICOLON'
)

t_PLUS = r'\+'
t_SEMICOLON = r';'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_program(p):
    '''program : expression SEMICOLON'''
    p[0] = ('PROGRAM', p[1])

def p_expression_plus(p):
    '''expression : expression PLUS term'''
    p[0] = ('+', p[1], p[3])

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_number(p):
    '''term : NUMBER'''
    p[0] = ('NUMBER', p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Test
data = "3 + 4;"
result = parser.parse(data, lexer=lexer)
print(result)
