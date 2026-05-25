def add_mul(a, b, c):
    out = (a + b) * c
    return out

val1 = int(input("enter the value1 :"))
val2 = int(input("enter the value2 :"))
val3 = int(input("enter the value3 :"))

result = add_mul(val1, val2, val3)

print("the result is :", result)