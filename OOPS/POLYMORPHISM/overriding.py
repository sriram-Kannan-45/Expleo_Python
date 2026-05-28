class Vehicle :

    def __init__ (self , name , color , price ):

        self.name = name 

        self.color = color

        self.price = price 
    
    def show(self) :

        print ("Details", self.name , self.color , self.price )

    def max_speed (self) :

        print("Vechicle Max speed is 150 ")

    def change_gear (self) :

        print("Vechicle change 6 gear ")


class Car (Vehicle) :

    def max_speed (self) :

        # super().max_speed()

        print("car max speed is 240 ")

    def change_gear (Self) :

        # super().change_gear()

        print("car chage the 7 gear")

car = Car("car 1" , "red" , 500)
car.show()
car.max_speed()
car.change_gear()

vechi = Vehicle("bike" , "black" , 7699)

vechi.show()

vechi.max_speed()