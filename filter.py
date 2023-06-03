students = [
    {"name": "ali", "house":"pakistan"},
    {"name": "akhtar", "house":"ind"},
    {"name": "saif", "house":"pakistan"},
    {"name": "khushi", "house":"bwp"},
    {"name": "husi", "house":"pakistan"}
]

def is_paki(s):
    return  s["house"] == "pakistan"
""" if s["house"] == "pakistan":
        return True
    else:
        return False
"""
pakistan = filter(is_paki, students)

for paki in pakistan:
    print(paki["name"])