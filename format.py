import re
"""
name = input("whats your name:").strip()
if "," in name:
    first, second = name.split(", ?")
    name = f"{first} {second}"
print(f"hello, {name}")
"""

#() in that re format expression can return a group of the values like split functions of strings

name = input("whats your name:").strip()
if matches := re.search (r"^(.+), *(.+)$", name):
    name= matches.groups(2) + "" + matches.group(1)
    #name = f"{last} {first}"
print(f"hello,{name}")
