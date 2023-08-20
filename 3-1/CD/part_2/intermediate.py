class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_var_counter = 0

    def generate(self, node):
        if node.type == "VariableDeclaration":
            for var in node.children:
                self.code.append(f"DECLARE {var}")

        elif node.type == "FunctionCall":
            args = ', '.join(node.children[1:])
            self.code.append(f"CALL {node.children[0]} WITH ARGS {args}")

        elif node.type == "WhileLoop":
            condition = ' '.join(node.children[:-1])
            self.code.append(f"LABEL start_while_{self.temp_var_counter}")
            self.code.append(f"IF NOT {condition} GOTO end_while_{self.temp_var_counter}")
            self.generate(node.children[-1])
            self.code.append(f"GOTO start_while_{self.temp_var_counter}")
            self.code.append(f"LABEL end_while_{self.temp_var_counter}")
            self.temp_var_counter += 1

        elif node.type == "IfStatement":
            condition = ' '.join(node.children[:-1])
            self.code.append(f"IF NOT {condition} GOTO end_if_{self.temp_var_counter}")
            self.generate(node.children[-1])
            self.code.append(f"LABEL end_if_{self.temp_var_counter}")
            self.temp_var_counter += 1

        # Recursively generate code for children
        for child in node.children:
            if isinstance(child, Node):
                self.generate(child)

    def get_code(self):
        return '\n'.join(self.code)
