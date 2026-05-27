str1 = input("Enter a string: ")
sub = input("Enter a substring to search: ")

pos = str1.rfind(sub)

print(pos)
print("Last occurrence of "+ sub + " is at index: " , pos)