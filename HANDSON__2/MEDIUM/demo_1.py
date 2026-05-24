age = int(input("Enter your age: "))

if age < 1:
    print("invlaid age")
elif age > 20:
    print("Not allowed")
elif age >= 1 and age <= 12:
    print("Cartoon club")
elif age > 12 and age <= 20:
    print("Teen club")