# import re

# def is_valid_variable_name(name):
#     pattern = r"^\$[a-zA-Z_][a-zA-Z0-9_]*#$"
#     return bool(re.match(pattern, name))

# # Test
# test_names = ["$variable#", "$_name1#", "$123invalid#", "$name@#", "name#",'name']
# for name in test_names:
#     print(f"'{name}' is valid? {is_valid_variable_name(name)}")

import re

def is_valid_variable_name(name):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, name))

# Test the function
print("var1",is_valid_variable_name("var1"))  # Should return True
print("_var",is_valid_variable_name("_var"))  # Should return True
print("2var",is_valid_variable_name("2var"))  # Should return False




def is_valid_special_variable_name(name):
    pattern = r"^\$[a-zA-Z_][a-zA-Z0-9_]*#$"
    return bool(re.match(pattern, name))

# Test the function
print("$var1#",is_valid_special_variable_name("$var1#"))  # Should return True
print("$_var#",is_valid_special_variable_name("$_var#"))  # Should return True
print("$2var#",is_valid_special_variable_name("$2var#"))  # Should return False