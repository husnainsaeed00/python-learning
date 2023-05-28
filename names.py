import sys

# dont try to worry about the error message , think like a problem solver.
# tell the user about the problem in the decent way so they dont panic
#try:
#    print("MY nme is ", sys.argv[1])
#except IndexError:
# print("you have forgot to enter the name in cmd of the progaram")
if len(sys.argv)< 2 :
    sys.exit("too few arguments")
elif len(sys.argv)>2 : 
    sys.exit("too many arguments")

print("my name is ", sys.argv[1])


# we have learned about the pakcage of Cowsay 

# Apis----pip install request
