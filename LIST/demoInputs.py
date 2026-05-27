# listA = []

# n = int (input("Enter the number of elements in the list: "))

# for i in range(0,n):

#     print("Enter element No - {} : ".format(i+1))
#     element = int(input())
#     listA.append(element)
# print("The list is : ", listA)

# #splict

# listB = input("Enter the elements of the list separated by space: ").split(" ")
# print("The list is : ", listB)

# #map

# listC = list(map(int, input("Enter the elements of the list separated by space: ").split(" ")))
# print("The list is : ", listC)

# #list comprehension

# listD = [x**2 for x in range(5)]
# print(listD)

# listE = [x if x == 2 else x*2 for x in range(10) ]
# print(listE)

# number = [x for x in range(10)]

# number1 = [x for x in number if x%2 == 0]
# print(number1)
# number2 = [x for x in number if x%2 != 0]
# print(number2)

product = eval(input("Enter the product of the list: "))
print(product)