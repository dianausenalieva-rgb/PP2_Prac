import shutil
import os

# 1
shutil.move("test.txt", "folder1/test.txt")

# 2
shutil.copy("folder1/test.txt", "copy.txt")

# 3
os.rename("copy.txt", "renamed.txt")

# 4
shutil.move("renamed.txt", "folder1/renamed.txt")

# 5
print(os.listdir("folder1"))