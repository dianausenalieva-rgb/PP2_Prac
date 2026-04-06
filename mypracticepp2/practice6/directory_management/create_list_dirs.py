import os

# 1
os.mkdir("folder1")

# 2
os.makedirs("a/b/c", exist_ok=True)

# 3
print(os.listdir("."))

# 4
print(os.getcwd())

# 5
os.chdir("folder1")
print(os.getcwd())