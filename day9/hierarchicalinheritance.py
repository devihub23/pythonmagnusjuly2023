class Teacher():
    def english(self):
        print("english teacher")
class Student1(Teacher):
    def first(self):
        print("first grade")
class Student2(Teacher):
    def second(self):
        print("second grade")
obj1=Student1()
obj2=Student2()
obj1.english()
obj2.english()
