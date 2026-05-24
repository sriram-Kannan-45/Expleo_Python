name = input("Enter customer name: ")
items = int(input("Enter number of items: "))

if items < 10:
    total = items * 12
elif items <= 99:
    total = items * 10
else:
    total = items * 7

print(name, total)