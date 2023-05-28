import csv

"""
with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name":row["name"], "home":row["home"]})
    # for line in file:
     #   name, house = line.strip().split(",")
    #    student = {"name": name, "house": house}
      #  students.append(student)

#def get_name(student):
#    return student["name"]


for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
"""
students = []
name = input("what is your name:")
home = input("where is your home:")

with open("stuents.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])