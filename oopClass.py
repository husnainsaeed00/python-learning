class  Student:
    def __init__(self,name, house):
            self.name = name
            self.house= house
    def __str__(self):
            return f"{self.name} from {self.house}"
def main():
    student =get_student()
    print(student)

#now we are goitn to study dictionaries in python
    
    
def get_student():
    student =Student()
    student.name = input("what is your name")
    student.house = input("what is your house")
    return student
#def get_name():
    #return(input("please enter your name:"))    

#def  get_house():
    #return(input("please enter your houe:"))  

if __name__ == "__main__":
    main()        