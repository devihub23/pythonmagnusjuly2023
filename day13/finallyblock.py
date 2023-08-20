class Sample:
    def m1(self):
        a = 10
        b = 0
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("zero division error")
        try:
            print(c)
        except NameError as e1:
            print(e1)
        finally:
            print("name error")
obj1=Sample()
obj1.m1()
