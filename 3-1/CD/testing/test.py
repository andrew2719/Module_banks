import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = [
    'INT', 'ID', 'NUMBER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'IF', 'ELSE', 'WHILE', 'PRINTF', 'SCANF',
    'COMMA', 'SEMICOLON', 'NOT_EQUALS', 'AND', 'OR', 'STRING', 'AMPERSAND'  # Added AMPERSAND here
]

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_COMMA = r','
t_SEMICOLON = r';'
t_NOT_EQUALS = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_STRING = r'\".*?\"'
t_AMPERSAND = r'&'
def t_PRINTF(t):
    r'printf'
    return t

def t_SCANF(t):
    r'scanf'
    return t

def t_INT(t):
    r'int'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Parser
# ... [Lexer code remains unchanged] ...
# ... [Lexer code remains unchanged] ...

# Parser
def p_program(p):
    'program : declaration_list'
    p[0] = {'type': 'program', 'children': p[1]}

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_declaration(p):
    '''declaration : INT ID_list SEMICOLON
                   | ID EQUALS expression SEMICOLON
                   | PRINTF LPAREN STRING RPAREN SEMICOLON
                   | PRINTF LPAREN STRING COMMA expression RPAREN SEMICOLON
                   | SCANF LPAREN STRING COMMA AMPERSAND ID RPAREN SEMICOLON
                   | IF LPAREN condition RPAREN LBRACE declaration_list RBRACE
                   | IF LPAREN condition RPAREN LBRACE declaration_list RBRACE ELSE LBRACE declaration_list RBRACE
                   | WHILE LPAREN condition RPAREN LBRACE declaration_list RBRACE'''
    if p[1] == 'int':
        p[0] = {'type': 'declaration', 'datatype': p[1], 'declarations': p[2]}
    elif p[1] == 'printf' and len(p) == 5:
        p[0] = {'type': 'printf', 'string': p[3]}
    elif p[1] == 'printf' and len(p) == 7:
        p[0] = {'type': 'printf', 'string': p[3], 'expression': p[5]}
    elif p[1] == 'scanf':
        p[0] = {'type': 'scanf', 'format': p[3], 'id': p[6]}
    elif p[1] == 'if' and len(p) == 8:
        p[0] = {'type': 'if', 'condition': p[3], 'body': p[6]}
    elif p[1] == 'if' and len(p) == 12:
        p[0] = {'type': 'if-else', 'condition': p[3], 'if_body': p[6], 'else_body': p[10]}
    elif p[1] == 'while':
        p[0] = {'type': 'while', 'condition': p[3], 'body': p[6]}
    else:
        p[0] = {'type': 'assignment', 'id': p[1], 'value': p[3]}

def p_ID_list(p):
    '''ID_list : ID_list COMMA ID
               | ID_list COMMA ID EQUALS expression
               | ID
               | ID EQUALS expression'''
    if len(p) == 2:
        p[0] = [{'type': 'id', 'value': p[1]}]
    elif len(p) == 4:
        p[0] = p[1] + [{'type': 'id', 'value': p[3]}]
    elif len(p) == 6:
        p[0] = p[1] + [{'type': 'assignment', 'id': p[3], 'value': p[5]}]
    else:
        p[0] = [{'type': 'assignment', 'id': p[1], 'value': p[3]}]

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term
                  | expression MOD term
                  | term'''
    if len(p) == 4:
        p[0] = {'type': 'binary_op', 'op': p[2], 'left': p[1], 'right': p[3]}
    else:
        p[0] = p[1]

def p_term(p):
    '''term : LPAREN expression RPAREN
            | NUMBER
            | ID'''
    if len(p) == 4:
        p[0] = p[2]
    elif isinstance(p[1], int):
        p[0] = {'type': 'number', 'value': p[1]}
    else:
        p[0] = {'type': 'id', 'value': p[1]}

def p_condition(p):
    '''condition : expression EQUALS expression
                 | expression NOT_EQUALS expression'''
    p[0] = {'type': 'condition', 'op': p[2], 'left': p[1], 'right': p[3]}

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# Test
data = '''int main() {
    int n, reversed = 0, remainder, original;

    printf("Enter an integer: ");
    scanf("%d", &n);

    original = n;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed) {
        printf("Palindrome\n");
    } else {
        printf("Not a Palindrome\n");
    }
}'''

result = parser.parse(data)
print(result)
