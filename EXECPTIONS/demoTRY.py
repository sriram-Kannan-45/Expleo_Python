try:

    a = int(input())
    b = int(input())
    c = a/b

except NameError:

    print("cannot divide with zero")


except Exception :

    print("error")
print("sucess")