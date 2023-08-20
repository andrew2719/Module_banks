class Optimizer:
    def __init__(self):
        self.constants = {}

    def optimize(self, intermediate_code):
        lines = intermediate_code.split('\n')
        optimized_lines = []

        for line in lines:
            # Constant Propagation
            for const_var, value in self.constants.items():
                line = line.replace(const_var, value)

            # Dead Code Elimination (simple version)
            if line.startswith("DECLARE"):
                var_name = line.split()[1]
                if var_name not in intermediate_code:
                    continue

            # Constant Folding (simple version for our code)
            if "=" in line and "+" in line:
                parts = line.split()
                if parts[2].isdigit() and parts[4].isdigit():
                    result = int(parts[2]) + int(parts[4])
                    line = f"{parts[0]} = {result}"
                    self.constants[parts[0]] = str(result)

            optimized_lines.append(line)

        return '\n'.join(optimized_lines)
