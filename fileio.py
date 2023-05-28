#name = input("what is your name?")



"""names=[]
#print(f"hello {names}")
for _ in range(3):
    name=input("what's your name: ")
    names.append(name)
for name in sorted(names):
    print(f"hello {name}")

#with open("names.txt", "a") as file:
#  file.write(f"{name}\n")
with open("names.txt", "r") as file:
#   lines = file.readlines()
    for line in file:
        print("hello", line.rstrip())

        """

names= []

with open ("names.txt",) as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"hello, {name}")