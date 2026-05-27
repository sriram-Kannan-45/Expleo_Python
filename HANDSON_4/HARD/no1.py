lower = 0
upper = 0
non_alpha = 0

str1 = input()

for i in str1:
    if i.isupper():
        upper += 1

    elif i.islower():
        lower += 1

    else:
        non_alpha += 1

print("Lower case letters: " , lower)
print("Upper case letters: " , upper)
print("Non-alphabetic characters: " , non_alpha)