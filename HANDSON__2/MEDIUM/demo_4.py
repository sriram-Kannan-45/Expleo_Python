total = int(input("Enter total animals: "))
rabbit = int(input("Enter rabbits: "))
deer = int(input("Enter deer: "))
birds = int(input("Enter birds: "))
squirrel = int(input("Enter squirrels: "))

count = rabbit + deer + birds + squirrel

if count > total:
    print("Counted wrongly")
elif count < total:
    print("Baby lion is mischievous")
else:
    print("Baby lion is well behaved")
