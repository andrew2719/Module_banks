import re

def is_valid_variable_name(name):
    pattern = r"^\$[a-zA-Z_][a-zA-Z0-9_]*#$"
    return bool(re.match(pattern, name))

# Test
test_names = ["$variable#", "$_name1#", "$123invalid#", "$name@#", "name#"]
for name in test_names:
    print(f"'{name}' is valid? {is_valid_variable_name(name)}")
