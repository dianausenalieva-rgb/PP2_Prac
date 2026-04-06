# Пример 1: Сравнение чисел
x = 10
y = 5
print(x > y)      # True
print(x == y)     # False
print(x != y)     # True
print(x <= 10)    # True
print(y >= 10)    # False

# Пример 2: Сравнение строк
name1 = "Alice"
name2 = "Bob"
print(name1 == "Alice")          # True
print(name1 != name2)            # True
print("apple" < "banana")        # True (лексикографическое сравнение)
print("A" < "a")                 # True (заглавные буквы идут раньше)

# Пример 3: Сравнение списков
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(list1 == list2)            # True (одинаковые значения)
print(list1 is list2)            # False (разные объекты)
print(list1 != list3)            # True
print([1, 2] < [1, 2, 3])        # True (короткий список меньше)

#4
a = 15
b = 20
c = 15
print(a == c and a < b)          # True
print(a > b or b > 10)           # True
print(not (a == b))              # True
print(10 <= a <= 20)             # True (a между 10 и 20)

#5
value = None
number = 42
text = "hello"
print(value is None)             # True
print(value is not None)         # False
print(type(number) == int)       # True
print(isinstance(text, str))     # True
print(isinstance(number, (int, float)))  # True