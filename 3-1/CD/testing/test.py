from ply import lex, yacc

# Token list
tokens = (
    'ID',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'MULTIPLY'
)

# Token rules
t_EQUALS = r'='
t_PLUS = r'\+'
t_MULTIPLY = r'\*'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

# Ignored characters
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_statement_assign(t):
    'statement : ID EQUALS expression'
    t[0] = ('=', t[1], t[3])

def p_expression_binop(t):
    '''expression : expression PLUS term
                  | term'''
    if len(t) == 4:
        t[0] = ('+', t[1], t[3])
    else:
        t[0] = t[1]

def p_term_binop(t):
    '''term : term MULTIPLY factor
            | factor'''
    if len(t) == 4:
        t[0] = ('*', t[1], t[3])
    else:
        t[0] = t[1]

def p_factor(t):
    '''factor : NUMBER
              | ID'''
    t[0] = t[1]

def p_error(t):
    print(f"Syntax error at '{t.value}'")

# Build the parser
parser = yacc.yacc()

# Test it out
data = "position = initial + rate * 60"

# Generate the parse tree
parse_tree = parser.parse(data)



print("Parse tree:", parse_tree)
