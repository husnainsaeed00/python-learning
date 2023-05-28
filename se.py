#students = ["ali", "ahmad", "abdul"]
#for student in students:
#for i in range(len(students)):
#   print(i,students[i])
    
#Dictionaries
"""students = {
    "ali":"pakistan",
    "umar":"pak", 
    "saif":"pak"
    }
#print(students["ali"])
for student in students:
    print(student, students[student], sep=",")...."""
    

students = [
    {"name": "ali", "house":"bwp", "pet":"dog"},
    {"name": "umar", "house":"bwp", "pet":"cat"},
    {"name": "ron", "house":"bwp", "pet":"dog"},
    {"name": "husi", "house":"bwp", "pet":None}
]

for student in students:
    print(student["name"], student["house"],student["pet"])