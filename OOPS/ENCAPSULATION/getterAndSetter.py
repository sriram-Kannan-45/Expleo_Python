class Student :

    def __init__ (self , name , age ):

        self.name = name 
        self._age = age 

    def get_age(self):

        return self._age 
    
    def set_age(self , age ):
        self._age = age 

stud = Student("Mary" , 14)

print ("Name : " , stud.name , stud.get_age())

stud.set_age(16)

print("Name : " , stud.name , stud.get_age())

