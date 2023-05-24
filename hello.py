
#--------------------------------------Strings----------------------------------------


#Ask for the the name of user / comments can be the pseudocode/ They can be the to do list of your program .
"""
thats the way for multiline comments
"""   
#name = input('Whats your name ohh boy:').strip().title()
# Srtip removes white spaces from the strings
#name = name.strip()
# it makes the first word of element capital
#name = name.capitalize()
# it makes in upper case
#name = name.title()
#Now say hello to the user

# Slit function splits the name on incounter of space into two parts and assigns it to two variables
#first,last = name.split(" ")
#print(f'Hello, {first} ')

# removes the white spaces from the user input and capatilizes it
#name = name.strip().title()
#print("hello", name)


#------------------------------------def Functions---------------------------------------------------
# incase if user doesnt entered a value as a parameter to the function
def main():
    hello()
    name = input('Whats your name ohh boy:').strip().title()
    #hello()
    #print(name)
    hello(name)

def hello(to="world"):
    print("hello", to)
main()




