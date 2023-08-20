class Sample:
    def m1(self):
        a = 10
        b = 0
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
        try:
            print(c)
        except NameError as e1:
            print(e1)

obj1=Sample()
obj1.m1()
