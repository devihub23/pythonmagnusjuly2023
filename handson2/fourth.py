a=int(input("enter the score a:"))
b=int(input("enter the score of b:"))
x=a+b
print(int(x))
if (a>300 or b>300) and x<500:
    print("Can Team up")
else:
    print("Cannot Team up")


