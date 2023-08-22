class Sample:
    def m1(self):
        print("M1")
    def m2(self):
        print("M2")
    def __init__(self,a,b):
        print(a+b)

obj1 = Sample(10,20)
obj1.m1()
obj1.m2()
