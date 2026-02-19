#print("Welcome to Python OOP Learning")

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def Display(self):
        print(f"{self.brand} costs {self.price}")

M1=Mobile("Iphone",83000)
M2=Mobile("Relame",15000)

M1.Display()
M2.Display()