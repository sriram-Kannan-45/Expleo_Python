class Example :

    def methods (self , a , b = None ):

        if b is None :

            print(f"single argument : {a}")
        
        elif isinstance (a , int) and isinstance (b , int):

            print(f"two integers : {a} , {b}")

        elif isinstance (a , str) and (b , str) :

            print(f"two strings {a} , {b}" )

        else :

            print(f"Mixed types : {a} , {b}")

obj = Example()

obj.methods(1)

obj.methods(1,2)

obj.methods("hi" , "hello")

obj.methods(1 , "hii")