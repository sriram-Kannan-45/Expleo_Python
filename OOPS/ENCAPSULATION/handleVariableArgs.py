class Circle :

    def __init__ (self , *argu) :

        if (len(argu) == 0 ):

            self.radius = 1.0 
            self.color = "red"

        elif len(argu) == 1 :

            self.radius = argu[0]
            self.color = "red"

        elif len(argu) == 2 :

            self.radius = argu[0]
            self.color = argu[1]

        else :

            raise ValueError ("Too many arguments")
        
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
