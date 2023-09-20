#Method - 1

class Shape:
   def __init__(self,a,b,constant):
       print(a*b*constant)
 
class triangle(Shape):
   def __init__(self,b,h):
       super().__init__(b,h,0.5)
class circle(Shape):
   def __init__(self,r):
       super().__init__(r,r,3.14)
class rect(Shape):
   def __init__(self,b,h):
       super().__init__(b,h,1)
       
print("Area of Triangle")
triangle(20,10)
print("Area of Circle")
circle(5)
print("Area of Rectangle")
rect(4,5)

#********************************************************************

#Method - 2

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
