class Circle :

    def __init__(self , radius = 1.0, color = "red"):

        self.radius = radius
        self.color = color


    def getRadius (self) :

        return self.radius

    def getColor (self) :

        return self.color
    
    def setRadius(self , radius) :

        self.radius = radius

    def setColor(self , color) :

        self.color = color

    def getArea (self) :

        return 3.14 * self.radius * self.radius
    
    def __str__ (self) :

        return "The radius is " + str(self.getRadius()) + \
               " and the color is " + self.getColor() + \
               " and the area is " + str(self.getArea())



circle1 = Circle()

print(circle1)

circle2 = Circle(2.5)

print(circle2)

circle3 = Circle(2.5 , "blue")

print(circle3)



        
