#1
def sum_all(*args):
    return sum(args)

#2
def print_names(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

#3
def average(*args):
    return sum(args) / len(args)

#4
def student_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

#5
def mix(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


print(sum_all(1, 2, 3))
print_names(name="Anna", age=20)
print(average(2, 4, 6))
student_info(name="Tom", grade="A")
mix(1, 2, 3, 4, x=5, y=6)