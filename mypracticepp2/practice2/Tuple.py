#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#3
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#4
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#6
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#7
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#8
fruits = ("apple", "banana", "cherry")
#9
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  #10
  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)