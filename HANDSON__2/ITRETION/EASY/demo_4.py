n = int(input("Enter number: "))

total = 0

for i in range(n, 0, -1):
    print(i, end=" ")
    total += i

print(",", total)