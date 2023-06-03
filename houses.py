students = [
    {"name": "hammad" , "house":"karachi"},
    {"name": "saif" , "house":"lahore"},
    {"name": "ahmad" , "house":"Bahawalpur"},
    {"name": "ali" , "house":"karachi"},
    {"name": "umair" , "house":"islamabbad"}
]

houses=set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)