import re

def lexer(code):
    token_specs = [
        ('INCLUDE', r'#include <[a-zA-Z_.]+>'),
        ('TYPE', r'\bint\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('NUMBER', r'\b\d+\b'),
        ('STRING_LITERAL', r'".*"'),
        ('OPEN_BRACE', r'\{'),
        ('CLOSE_BRACE', r'\}'),
        ('OPEN_PAREN', r'\('),
        ('CLOSE_PAREN', r'\)'),
        ('SEMI_COLON', r';'),
        ('EQUAL', r'='),
        ('PLUS', r'\+'),
        ('MULTIPLY', r'\*'),
        ('MODULO', r'%'),
        ('DIVIDE', r'/'),
        ('EQUAL_EQUAL', r'=='),
        ('NOT_EQUAL', r'!='),
        ('COMMA', r','),
        ('WHITESPACE', r'\s+'),
        ('OTHER', r'.')
    ]

    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    get_token = re.compile(token_regex).match

    position = 0
    tokens = []
    while position < len(code):
        match = get_token(code, position)
        if match:
            kind = match.lastgroup
            value = match.group(kind)
            if kind != 'WHITESPACE':  # Ignore whitespace
                tokens.append((kind, value))
            position = match.end()
        else:
            raise RuntimeError(f"Unexpected character at {position}")

    return tokens
