import shutil
import os

# 1
shutil.copy("test.txt", "copy.txt")

# 2
shutil.copyfile("test.txt", "copy2.txt")

# 3
shutil.move("copy.txt", "moved.txt")

# 4
if os.path.exists("copy2.txt"):
    os.remove("copy2.txt")

# 5
if os.path.exists("moved.txt"):
    os.remove("moved.txt")