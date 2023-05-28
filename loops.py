
#while loop
#i=4
#while i !=0:
#   print("meow")
#   i = i-1

#For loop ----
# --------

#for  i in (0,1,10000):
"""while True:
    poo = int(input("whats the poo?"))
    if poo<0:
        continue
    else:
        break

for _ in range(poo):
    print("mew")


#escape sequences \n creates a new line inside the string and the end function makes the extra line disapear
#print("mew\n" *6, end="")"""

def main():
    number = get_number()
    mew(number)

def get_number():
    while True:
        n= int(input("whats is the number:"))
        if n>0: 
            return n

def mew(n):
    for _ in range(n):
        print("mew")

main()