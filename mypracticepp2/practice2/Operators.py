#1
print(10 + 5)
#2
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
#3
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#4
x = 12
y = 5

print(x / y)
#5
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
#6
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
#7
x = 5

print(x < 5 or x > 10)
#8
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#9
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)
#10
print(6 ^ 3)