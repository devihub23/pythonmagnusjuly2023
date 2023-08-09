a=int(input("employee's salary a:"))
b=int(input("employee's year of service b:"))
x=a*5/100
bonus=a+x
if b>=5:
    print("emplolyee get 5%bonus")
    print(int(x))
    print("bonus amount:"+str(x))
    print(int(bonus))
    print("salary including bonus:"+str(bonus))

else:
    print("no bonus")



