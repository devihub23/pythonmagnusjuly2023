class Grandparent:
    def a1(self):
        print("3 assets")
class Father(Grandparent):
    def a2(self):
        print("4 assets")
class Son(Father):
    def a3(self):
        print("1 assets")
obj1=Son()
obj1.a1()
obj1.a2()
obj1.a3()
obj2=Father()
obj2.a1()
obj2.a2()
obj3=Grandparent()
obj3.a1()

