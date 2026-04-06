#1 
doubled = list(map(lambda x: x * 2, numbers)
)
print(doubled)

#2 
plus_one = list(map(lambda x: x + 1, numbers))
print(plus_one)

#3 
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings)

#4 
squares = list(map(lambda x: x * x, numbers))
print(squares)

#5 
neg = list(map(lambda x: -x, numbers))
print(neg)