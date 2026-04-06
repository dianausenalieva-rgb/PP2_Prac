#1
class Father:
    def skill(self):
        print("Driving")

#2
class Mother:
    def skill(self):
        print("Cooking")

#3
class Child(Father, Mother):
    pass