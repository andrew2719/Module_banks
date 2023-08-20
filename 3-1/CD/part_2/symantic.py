class SemanticAnalyzer:
    def __init__(self):
        self.declared_variables = set()

    def analyze(self, node):
        if node.type == "VariableDeclaration":
            for var in node.children:
                if var in self.declared_variables:
                    raise Exception(f"Semantic Error: Variable {var} redeclared.")
                self.declared_variables.add(var)
        elif node.type == "FunctionCall":
            # For simplicity, we're not checking function arguments
            if node.children[0] not in ["printf", "scanf"]:
                raise Exception(f"Semantic Error: Unknown function {node.children[0]}")
        elif node.type in ["WhileLoop", "IfStatement"]:
            # Check conditions, for simplicity, we're just checking if variables are declared
            for condition_part in node.children[:-1]:
                if condition_part.isidentifier() and condition_part not in self.declared_variables:
                    raise Exception(f"Semantic Error: Undeclared variable {condition_part}")
        # Recursively analyze children
        for child in node.children:
            if isinstance(child, Node):
                self.analyze(child)
