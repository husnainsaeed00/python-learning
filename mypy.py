"""fhgfhgfhgfhgjhfghf


def meow (n: int):
    for _ in range(n):
        print("meow ")

# mypy command in the terminal window can help you with errors understanding easily. it describes errors better
number = int(input("number:"))
meow(number)

"""

import sys 
if len( sys.argv) == 1:
    print ("meow")
else:
    print("usage: mypy.py")