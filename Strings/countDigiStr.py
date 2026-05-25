name = input()

digit = 0

letter = 0

for i in name :

    if i.isnumeric():
        digit += 1
    elif i.isalpha():
       letter += 1
    else:
        pass

print(digit)
print(letter)