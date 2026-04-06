# 1
names = ["A", "B", "C"]
for i, name in enumerate(names):
    print(i, name)

# 2
nums = [10, 20, 30]
for i, n in enumerate(nums, start=5):
    print(i, n)

# 3
a = [1, 2, 3]
b = ["a", "b", "c"]
print(list(zip(a, b)))

# 4
names = ["A", "B"]
scores = [90, 80]
for n, s in zip(names, scores):
    print(n, s)

# 5
a = [1, 2]
b = [3, 4]
c = [5, 6]
print(list(zip(a, b, c)))