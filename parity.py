#
#if x % 2 == 0:
#    print("x is an even number")
#$else:
 #    print("x is an odd number")
def main():
    x = int(input("whats x:"))
    if is_even(x):
        print("x is an even number")
    else:
        print("x is an odd number")

def is_even(n):
# now the condition in the braces will return a value it could be a True or Flase 
    return (n % 2 ==0)    
#return True if n % 2 == 0 else False
    #if n % 2 == 0:
    #    return True
    #else:
    #    return False

main()