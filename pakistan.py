students = [
    {"name": "ali", "house":"pakistan"},
    {"name": "akhtar", "house":"ind"},
    {"name": "saif", "house":"pakistan"},
    {"name": "khushi", "house":"bwp"},
    {"name": "husi", "house":"pakistan"}
]

paki = [
    student["name"] for student in students if student["house"] == "pakistan"
]

for paki in sorted(paki):
    print(paki)