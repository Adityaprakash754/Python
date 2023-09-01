import math

class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showArea(self):
        print("The area of the ", self.name , " is " , self.area , "units")

class Circle(Shape):
    def __init__(self,radius):
        self.area = 0
        self.name = "Circle"
        self.radius = radius
    
    def calcArea(self):
        self.area = math.pi * self.radius * self.radius 

class Rectangle(Shape):    
    def __init__(self,length,breadth):       
        self.area = 0        
        self.name = "Rectangle"       
        self.length = length        
        self.breadth = breadth   

    def calcArea(self):        
        self.area = self.length * self.breadth
            
class Triangle(Shape):    
    def __init__(self,base,height):        
        self.area = 0        
        self.name = "Triangle"        
        self.base = base        
        self.height = height            
        
    def calcArea(self):        
        self.area = self.base * self.height / 2

c = Circle(5)
c.calcArea()
c.showArea()

r = Rectangle(5,4)
r.calcArea()
r.showArea()

t = Triangle(3,4)
t.calcArea()
t.showArea()