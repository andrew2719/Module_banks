class Node:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children if children is not None else []

class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def parse(self):
        return self.function_definition()

    def function_definition(self):
        if self.current_token == "int":
            self.next_token()
            if self.current_token == "main":
                self.next_token()
                if self.current_token == "(":
                    self.next_token()
                    if self.current_token == ")":
                        self.next_token()
                        return Node("FunctionDefinition", [self.block()])
                    else:
                        raise Exception("Expected )")
                else:
                    raise Exception("Expected (")
            else:
                raise Exception("Expected main")
        else:
            raise Exception("Expected int")

    def block(self):
        statements = []
        if self.current_token == "{":
            self.next_token()
            while self.current_token != "}":
                statements.append(self.statement())
            self.next_token()
        else:
            raise Exception("Expected {")
        return Node("Block", statements)

    def statement(self):
        if self.current_token == "int":
            return self.variable_declaration()
        elif self.current_token in ["printf", "scanf"]:
            return self.function_call()
        elif self.current_token == "while":
            return self.while_loop()
        elif self.current_token == "if":
            return self.if_statement()
        else:
            raise Exception("Unknown statement")

    def variable_declaration(self):
        variables = []
        self.next_token()
        while self.current_token != ";":
            if self.current_token not in [",", "="]:
                variables.append(self.current_token)
            self.next_token()
        self.next_token()
        return Node("VariableDeclaration", variables)

    def function_call(self):
        name = self.current_token
        self.next_token()
        args = []
        if self.current_token == "(":
            while self.current_token != ")":
                if self.current_token not in [","]:
                    args.append(self.current_token)
                self.next_token()
            self.next_token()
            if self.current_token == ";":
                self.next_token()
            else:
                raise Exception("Expected ;")
        else:
            raise Exception("Expected (")
        return Node("FunctionCall", [name] + args)

    def while_loop(self):
        self.next_token()
        condition = []
        if self.current_token == "(":
            while self.current_token != ")":
                condition.append(self.current_token)
                self.next_token()
            self.next_token()
        else:
            raise Exception("Expected (")
        return Node("WhileLoop", condition + [self.block()])

    def if_statement(self):
        self.next_token()
        condition = []
        if self.current_token == "(":
            while self.current_token != ")":
                condition.append(self.current_token)
                self.next_token()
            self.next_token()
        else:
            raise Exception("Expected (")
        return Node("IfStatement", condition + [self.block()])
