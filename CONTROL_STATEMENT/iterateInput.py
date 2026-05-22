n = int(input())

i=1

sum = 0

while i<=n :

    num = int(input())

    if num == -1 :

        break
    
    else :

        sum = sum + num
    
    i = i+1 

print("The sum of user input is:", sum)