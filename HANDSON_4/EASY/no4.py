str1 = input("Enter a string: ").split(" ")

for i in str1:

    for j in i:

        if j.isnumeric():

            print(i)
            break
    