str1 = input("Enter a string: ")

for i in str1:

    if not i.isalpha() and not i.isspace():
        str1 = str1.replace(i, "#")

print(str1)
