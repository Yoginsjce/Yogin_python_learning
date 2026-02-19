class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def __init__(self,name):
        self.name=name

    def ride(self):
        print("The bike is riding")

B1=Bike("RE")
B1.start()
B1.ride()

        