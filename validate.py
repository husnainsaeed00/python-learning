
#regrular expressions

#?= 0 times or 1 repetitions

import re
email = input("what is your email address:").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net)$",email,re.IGNORECASE):
    print("valid")
else:
    print("invalid")



    
"""email = input("what is your email address:").strip()
username,domain = email.split("@")
if username and domain.endswith(".com"):
    print("valid")
else:
    print("Invalid")
    
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid")
"""