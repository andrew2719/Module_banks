import lex

def parser(tokens):
    iterator = iter(tokens)
    current_token = next(iterator, None)

    def accept(token_type):
        nonlocal current_token
        if current_token and current_token[0] == token_type:
            current_token = next(iterator, None)
            return True
        return False

    def expect(token_type):
        if not accept(token_type):
            raise RuntimeError(f"Expected {token_type} but found {current_token}")

    def program():
        return {
            'includes': includes(),
            'functions': functions()
        }

    def includes():
        incs = []
        while accept('INCLUDE'):
            incs.append({'type': 'include', 'value': current_token[1]})
        return incs

    def functions():
        funcs = []
        while current_token and current_token[0] == 'TYPE':
            funcs.append(function())
        return funcs

    def function():
        expect('TYPE')
        name = current_token[1]
        expect('IDENTIFIER')
        expect('OPEN_PAREN')
        params = []  # For simplicity, we're not parsing function parameters
        expect('CLOSE_PAREN')
        expect('OPEN_BRACE')
        body = statements()
        return {
            'type': 'function',
            'name': name,
            'params': params,
            'body': body
        }

    def statements():
        stmts = []
        while current_token and current_token[0] not in ['CLOSE_BRACE']:
            stmts.append(statement())
        expect('CLOSE_BRACE')
        return stmts

    def statement():
        if current_token[0] == 'TYPE':
            return declaration()
        elif current_token[0] == 'IDENTIFIER' and current_token[1] in ['printf', 'scanf']:
            return function_call()
        elif current_token[0] == 'IDENTIFIER':
            return assignment()
        elif accept('WHILE'):
            return while_loop()
        elif accept('IF'):
            return if_statement()
        elif accept('RETURN'):
            return return_statement()
        else:
            raise RuntimeError(f"Unexpected token {current_token} in statement")

    def declaration():
        expect('TYPE')
        name = current_token[1]
        expect('IDENTIFIER')
        expect('EQUAL')
        expr = expression()
        expect('SEMI_COLON')
        return {
            'type': 'declaration',
            'name': name,
            'value': expr
        }

    def assignment():
        name = current_token[1]
        expect('IDENTIFIER')
        expect('EQUAL')
        expr = expression()
        expect('SEMI_COLON')
        return {
            'type': 'assignment',
            'name': name,
            'value': expr
        }

    def while_loop():
        expect('OPEN_PAREN')
        cond = condition()
        expect('CLOSE_PAREN')
        body = statements()
        return {
            'type': 'while_loop',
            'condition': cond,
            'body': body
        }

    def if_statement():
        expect('OPEN_PAREN')
        cond = condition()
        expect('CLOSE_PAREN')
        true_body = statement()
        false_body = None
        if accept('ELSE'):
            false_body = statement()
        return {
            'type': 'if_statement',
            'condition': cond,
            'true_body': true_body,
            'false_body': false_body
        }

    def return_statement():
        expr = expression()
        expect('SEMI_COLON')
        return {
            'type': 'return_statement',
            'value': expr
        }

    def condition():
        left = expression()
        if accept('EQUAL_EQUAL'):
            op = '=='
        elif accept('NOT_EQUAL'):
            op = '!='
        else:
            raise RuntimeError(f"Unexpected token {current_token} in condition")
        right = expression()
        return {
            'type': 'condition',
            'left': left,
            'operator': op,
            'right': right
        }

    def function_call():
        name = current_token[1]
        expect('IDENTIFIER')
        expect('OPEN_PAREN')
        args = []
        while not accept('CLOSE_PAREN'):
            args.append(expression())
            if not accept('COMMA'):
                break
        expect('SEMI_COLON')
        return {
            'type': 'function_call',
            'name': name,
            'args': args
        }


    def expression():
        if current_token[0] == 'NUMBER':
            value = current_token[1]
            accept('NUMBER')
            return {
                'type': 'number',
                'value': value
            }
        elif current_token[0] == 'IDENTIFIER':
            value = current_token[1]
            accept('IDENTIFIER')
            return {
                'type': 'identifier',
                'value': value
            }
        else:
            raise RuntimeError(f"Unexpected token {current_token} in expression")

    return program()

# Test
code = """
#include <stdio.h>

int main() {
    int n, reversed = 0, remainder, original;

    printf("Enter an integer: ");
    scanf("%d", &n);

    original = n;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed)
        printf("%d is a palindrome.", original);
    else
        printf("%d is not a palindrome.", original);

    return 0;
}
"""

tokens = lex.lexer(code)
for token in tokens:
    print(token)
tree = parser(tokens)
print(tree)
