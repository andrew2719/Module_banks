from ply import lex, yacc
data = '''
int main() {
    int n, reversed = 0, remainder, original;
    n = 121;
    original = n;
    while(n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n = n/10;
    }
    if(original == reversed) {
        return 0;
    }
    else{
        return 1;
    }
}
'''
# Token list
tokens = (
    'ID',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'SEMICOLON',
    'COMMA',
    'INT',
    'RETURN',
    'IF',
    'ELSE',
    'WHILE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'EQUALITY',
    'NOT_EQUAL'
)

# Token rules
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'  # Corrected the division operator
t_MODULO = r'%'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALITY = r'=='
t_NOT_EQUAL = r'!='

# Keywords
reserved = {
    'int': 'INT',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Ignored characters
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# print the genreated tokens
lexer.input(data)
for token in lexer:
    print(token)

# Parsing rules
def p_program(t):
    '''program : function
               | function program'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[2]

def p_function(t):
    'function : INT ID LPAREN RPAREN LBRACE statements RBRACE'
    t[0] = ('function', t[2], t[6])

def p_statements(t):
    '''statements : statement
                  | statement statements'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[2]

def p_statement(t):
    '''statement : declaration
                 | assignment
                 | if_statement
                 | while_loop
                 | return_statement'''
    t[0] = t[1]

def p_declaration(t):
    '''declaration : INT declaration_list SEMICOLON'''
    t[0] = ('declaration', t[1], t[2])

def p_declaration_list(t):
    '''declaration_list : declaration_item
                        | declaration_item COMMA declaration_list'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = [t[1]] + t[3]

def p_declaration_item(t):
    '''declaration_item : ID
                        | ID EQUALS expression'''
    if len(t) == 2:
        t[0] = ('var', t[1])
    else:
        t[0] = ('var_init', t[1], t[3])

def p_assignment(t):
    'assignment : ID EQUALS expression SEMICOLON'
    t[0] = ('assignment', t[1], t[3])

def p_if_statement(t):
    '''if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if len(t) == 8:
        t[0] = ('if', t[3], t[6])
    else:
        t[0] = ('if-else', t[3], t[6], t[10])


def p_while_loop(t):
    'while_loop : WHILE LPAREN condition RPAREN LBRACE statements RBRACE'
    t[0] = ('while', t[3], t[6])

def p_return_statement(t):
    'return_statement : RETURN expression SEMICOLON'
    t[0] = ('return', t[2])

def p_condition(t):
    '''condition : expression EQUALITY expression
                 | expression NOT_EQUAL expression'''
    t[0] = (t[2], t[1], t[3])

def p_expression(t):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(t) == 4:
        t[0] = (t[2], t[1], t[3])
    else:
        t[0] = t[1]

def p_term(t):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | term MODULO factor
            | factor'''
    if len(t) == 4:
        t[0] = (t[2], t[1], t[3])
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


# Generate the parse tree
parse_tree = parser.parse(data)


print("Parse tree:", parse_tree)
