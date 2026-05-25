n = input("Enter a string: ")

n1 = n[::-1]

if n.__eq__(n1):
    print("The string is a palindrome.")
    print("The reverse of the string is: ", n1)
else:
    print("The string is not a palindrome.")
    print("The reverse of the string is: ", n1)