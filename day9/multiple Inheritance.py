class Father:
    def home(self):
        print("2 homes")
class Mother:
    def car(self):
        print("2 cars")
class Son(Father,Mother):
    def cash(self):
        print("1 million")
obj1=Son()
obj1.home()
obj1.car()
obj1.cash()
