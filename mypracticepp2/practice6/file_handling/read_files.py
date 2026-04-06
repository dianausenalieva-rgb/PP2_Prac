# 1
with open("test.txt", "r") as f:
    print(f.read())

# 2
with open("test.txt", "r") as f:
    print(f.readline())

# 3
with open("test.txt", "r") as f:
    print(f.readline())
    print(f.readline())

# 4
with open("test.txt", "r") as f:
    for line in f:
        print(line)

# 5
with open("test.txt", "r") as f:
    print(f.readlines())