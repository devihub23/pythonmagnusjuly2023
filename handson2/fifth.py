a=int(input("first angle of triangle a:"))
b=int(input("second angle of triangle b:"))
c=int(input("third angle of triangle c:"))
x=a+b+c
print(int(x))
if x==180:
    print("triangle")
else:
    print("not a triangle")

