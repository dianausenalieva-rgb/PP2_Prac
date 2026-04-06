#1 
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)

#2 
words = ["apple", "pie", "banana", "cherry"]
sorted_by_len = sorted(words, key=lambda x: len(x))
print(sorted_by_len)

#3 
nums = [-4, -1, 3, 2, -9]
sorted_by_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_by_abs)

#4 сортировка строк в обратном порядке
sorted_desc = sorted(words, reverse=True)
print(sorted_desc)

#5 
sorted_first = sorted(words, key=lambda x: x[0])
print(sorted_first)