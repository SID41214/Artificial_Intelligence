a = 100
b = 50
c = 50
if (a < b):
    print("a is greater than b")
    if (c > a):
        print("c is greater than a")
    else:
        print("c is smaller")

elif(a == b and b == c):
    print("something is equal")

else:
    print("a is smaller than b")

