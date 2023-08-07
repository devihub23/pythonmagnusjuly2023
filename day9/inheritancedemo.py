class Sample:
    def m1(self):
        print("m1 function")
class Demo(Sample):
    def m2(self):
        print("m2 function")
obj1=Demo()
obj1.m1()
obj1.m2()
