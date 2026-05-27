import traceback

try :

    num = int(input("enter a positive integer : "))

    if num <= 0 :

        raise ValueError ("raise")
    
except ValueError  :

    error_msg = traceback.format_exc()
    print(error_msg)

print("i am sucessfully")