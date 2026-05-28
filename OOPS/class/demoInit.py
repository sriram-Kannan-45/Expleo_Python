class Myclass:

    def __init__(self , name):
        
        self.name = name 

    def __init__(self , nam , names):
        
        self.nam = nam
        self.names = names

    def dipalyName (self) :

        print ("hii - " , self.name)

obj = Myclass("titoo")

obj.dipalyName()