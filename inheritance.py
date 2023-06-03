class Wizard:
    def __init__ (self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name

class Student:
    def __intit__ (self, name, house):
        super().__init__(name)
        self.house = house


class Professor:
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
wizard = Wizard("albus")
student = Student("ali", "ahmad")
professor = Professor("saeed", "aftab")