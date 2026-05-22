num = int(input("Enter a number: "))

fact = 1

if num==0 or num == 1:
    
    fact=1

else:
    
    for i in range(2,num+1):

        fact = fact * i 

print ("factorial is",fact)

