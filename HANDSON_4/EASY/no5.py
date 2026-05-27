upper = ""
lower = ""

str1 = input("Enter a string: ")

for i in str1:

    if i.isupper():
        upper += i

    elif i.islower():
        lower += i
print(lower+upper)