class Car_2022():
    def roof(self):
        print("sun glasses")
class Car_2023(Car_2022):
    def roof(self):
        print("panaromic glasses")
        super().roof()
obj1=Car_2023()
obj1.roof()

