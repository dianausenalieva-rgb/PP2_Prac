#1
class Person:
    def printname(self):
        print("Person")

#2
class Student(Person):
    def printname(self):
        print("Student")

#3
class Teacher(Person):
    def printname(self):
        print("Teacher")

#4
class Worker(Person):
    def printname(self):
        print("Worker")

#5
class Child(Person):
    def printname(self):
        print("Child")