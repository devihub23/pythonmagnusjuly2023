class EligibleError(Exception):
    pass
class Sample:
    def m1(self,age,percentage):
        if age<18 or percentage<60:
           raise EligibleError("not eligible")
        else:
            print("eligible")
obj1=Sample()
obj1.m1(19,70)

