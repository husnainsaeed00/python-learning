try:
    x = int(input("whta is the x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is the  {x}")