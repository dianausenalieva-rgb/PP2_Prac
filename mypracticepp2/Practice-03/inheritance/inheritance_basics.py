#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

#2
class Student(Person):
    pass

#3
class Teacher(Person):
    pass

#4
class Worker(Person):
    pass

#5
class Child(Person):
    pass