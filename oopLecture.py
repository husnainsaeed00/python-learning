# we are going to study tuples , tuples are immuatable we can't use em like list 
def main():
    student =get_student()
    if student["name"] == "Padma":
        student["house"] = "bahawalpur"
    #name =get_name()
    #house=get_house()
    print(f"{student['name']} from {student['house']}")

#now we are goitn to study dictionaries in python
    
    
def get_student():
    
    name= input("please enter name:")
    house= input("please enter house:")
    return {"name": name, "house": house}
#def get_name():
    #return(input("please enter your name:"))    

#def  get_house():
    #return(input("please enter your houe:"))  

if __name__ == "__main__":
    main()    