
from threading import Thread
from time import sleep
class Simple(Thread):
    def m1(self):
        for i in range(1,21):
            print(i)
            sleep(1)
    def run(self):
        self.m1()
class Demo(Thread):
    def run(self):
        for i in range(21,41):
            print(i)
            sleep(1)
obj1=Simple()
obj2=Demo()
obj1.start()
obj2.start()
obj1.join()
print("end of the pgm")
