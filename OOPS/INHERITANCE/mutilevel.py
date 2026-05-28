class Student :

    def getStudentInfo ( self ) :

        self.__rollno = input ("Enter Roll Number. ")
        self.__name = input("Enter Name: ")

    def printStuentInfo (self) :

        print("Roll Number : " , self.__rollno , "\nName : " , self.__name)

class Marks (Student):

    def getMarks(self) :

        self.getStudentInfo()

        self.__m1 = float(input("mark 1 : "))
        self.__m2 = float(input("mark 2 : "))
        self.__m3 = float(input("mark 3 : "))

    def printMark(self) :

        self.printStuentInfo()

        print("mark 1 : ", self.__m1)
        print("mark 2 : ", self.__m2)
        print("mark 3 : ", self.__m3)

    def calTotal (self) :

        return self.__m1 + self.__m2 + self.__m3 
    
class results (Marks) :

    def result (self) :

        self.getMarks()
        self.__total = self.calTotal()

    def putResult (self) :

        self.printMark()

        print ("Total mark : " , self.__total)

obj = results()

obj.result()
obj.putResult()