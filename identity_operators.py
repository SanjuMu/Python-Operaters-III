x = 10
if(type(x) is int):
    print("True")

else:
    print("False")


x = 20
y = 20

if(x is y):
    print("x & y have the SAME value")
y = 30

if (x is not y):
    print("x & y have DIFFERENT value")