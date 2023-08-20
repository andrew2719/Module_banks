class CodeGenerator:
    def __init__(self):
        self.assembly_code = []
        self.register_counter = 0

    def generate(self, intermediate_code):
        lines = intermediate_code.split('\n')
        for line in lines:
            if line.startswith("DECLARE"):
                var_name = line.split()[1]
                self.assembly_code.append(f"ALLOC {var_name}")

            elif line.startswith("CALL"):
                parts = line.split()
                func_name = parts[1]
                args = ' '.join(parts[4:])
                self.assembly_code.append(f"LOAD {args}")
                self.assembly_code.append(f"CALL {func_name}")

            elif line.startswith("LABEL"):
                label = line.split()[1]
                self.assembly_code.append(f"{label}:")

            elif line.startswith("IF NOT"):
                parts = line.split()
                condition = parts[2]
                label = parts[5]
                self.assembly_code.append(f"JUMP-NOT {condition} {label}")

            elif line.startswith("GOTO"):
                label = line.split()[1]
                self.assembly_code.append(f"JUMP {label}")

            # ... Add more translations as needed

    def get_assembly(self):
        return '\n'.join(self.assembly_code)
