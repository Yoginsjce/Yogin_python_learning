class Shape:
    def calc_area(self):
        print("Area Calculated")

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calc_area(self):
        print(f"Area of circle is {(22/7)*self.radius*self.radius}")

class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def calc_area(self):
        print(f"Area of rectangle is {self.l*self.b}")

R=Rectangle(3,2)
C=Circle(7)

R.calc_area()
C.calc_area()