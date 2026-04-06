#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#4
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#6
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#7
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  #8
  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#9
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#10
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)