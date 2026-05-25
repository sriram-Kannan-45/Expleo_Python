def add_mult(n1, n2, n3=1):

    out = (n1 + n2) * n3 

    return out
val1 = int(input("enter the value1 :"))
val2 = int(input("enter the value2 :"))
val3 = int(input("enter the value3 :"))
result = add_mult(val1, val2, val3)
print("the result is :", result)
result = add_mult(val1, val2)
print("the result is :", result)