import math

 def add_nunber(n):
    for i in range (n+1):
        if i %2!=0:
            yield math.sqrt(i)

    for i in add_nunber(n):
        print(i)


