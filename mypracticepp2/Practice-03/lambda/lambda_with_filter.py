#1 filter: только нечётные
odd = list(filter(lambda x: x % 2 != 0, numbers))
print(odd)

#2 filter: только чётные
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

#3 filter: > 4
greater4 = list(filter(lambda x: x > 4, numbers))
print(greater4)

#4 filter: < 5
less5 = list(filter(lambda x: x < 5, numbers))
print(less5)

#5 filter: числа, делящиеся на 3
div3 = list(filter(lambda x: x % 3 == 0, numbers))
print(div3)