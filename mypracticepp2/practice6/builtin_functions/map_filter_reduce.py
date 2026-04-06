
# 1
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))

# 2
nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))

# 3
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, nums))

# 4
nums = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, nums)))

# 5
nums = [5, 10, 15]
print(list(filter(lambda x: x > 7, nums)))