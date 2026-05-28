class num :

    def __init__(self):

        self.x = 20
        self.y = 10

class add (num) :

    def findSum (self) :

        self.z = self.x + self.y

        print (self.z)

class sub(num):
    
    def findSub(self):

        self.z = self.x - self.y

        print(self.z)
        
ob1=add()
ob2=sub()
ob1.findSum()
ob2.findSub()