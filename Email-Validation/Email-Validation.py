import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

email = input("Enter an Email to validate: ")
if validate_email(email):
    print("Valid Email")    
else: 
     print("Invalid Email")