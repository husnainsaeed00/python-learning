name = input(" Whats your name?")

#if name == "Harry":
 #   print("Pakistan")
#elif name == "Husanain":
 #   print("BWP")
#elif name == "Ali":
 #   print("Dera Nawab")
#else:
#    print("Who")
match name:
    case "harry":
        print("Pak")
    case "ron":
        print("nz")
    case "ali":
        print("ind")
    case _:
        print("who")
    
        