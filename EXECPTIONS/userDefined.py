class Error(Exception) :
    pass

class ValueTooSmallError (Error) :
    pass
class ValueTooLargeError(Error):
    pass

num = 10

while True :

    try :

        i_num = int(input("enter the number"))

        if i_num < num :

            raise ValueTooSmallError
        elif i_num > num :

            raise ValueTooLargeError
        
        break
    except ValueTooLargeError :

        print ("large")
    
    except ValueTooSmallError :

        print ("small")

print("done")
    