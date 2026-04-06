# 1
with open("test.txt", "w") as f:
    f.write("Hello")

# 2
with open("test.txt", "a") as f:
    f.write(" World")

# 3
with open("new.txt", "x") as f:
    f.write("New file")

# 4
with open("test.txt", "w") as f:
    f.write("Line1\nLine2")

# 5
with open("test.txt", "a") as f:
    f.write("\nLine3")