class Shape:                      # superclass
    def __init__(self):      
        self.color = (0,0,0)

class Rectangle(Shape):           # subclass
    def __init__(self, w, h):    
        Shape.__init__(self)      # Need to call constructor function of superclass while inheriting to a subclass
        self.width = w
        self.height = h
    
    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(20,10)
print(rect1.height)
print(rect1.area())
print(rect1.color)