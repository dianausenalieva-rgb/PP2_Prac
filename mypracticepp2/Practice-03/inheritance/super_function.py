#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

#2
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#3
class Teacher(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#4
class Worker(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#5
class Child(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)