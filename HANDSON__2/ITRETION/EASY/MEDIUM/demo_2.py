num = input("Enter a five digit number: ")

if len(num) != 5:
    print("Not a valid number")

else:
    print(num[::-1])