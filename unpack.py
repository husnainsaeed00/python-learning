#first , _ = input("what is your name:").split(" ")
#print(f"hwllo, {first}")

"""def total(galleons, sickles,knuts):
    return( galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}


print(total(**coins), "knuts")

"""

def f(*args,**kwargs):
    print("possional:", kwargs)

f([])