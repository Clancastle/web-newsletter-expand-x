import re

# Validate strong password
password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
print(re.match(password_pattern, 'secret')) # Returns None
print(re.match(password_pattern, '-Secr3t.')) # Returns Match object

