demoList = []

while True:

    print("enter the choice:")
    print("1. append an element \n2. insert an element \n3. append a list to the given list \n4.Modify an existing element \n5. delete an existing element from the position \n6. delete an existing element with given value \n7. sort the list in ascending order \n8. sort the list in descending order \n9. display the list \n10. exit")

    choice = int(input("enter the choice: "))

    if choice == 1:

        n = int (input("enter the element to be appended: "))
        demoList.append(n)
    
    elif choice == 2:
        n = int (input("enter the element to be inserted: "))
        pos = int (input("enter the position to be inserted: "))
        demoList.insert(pos, n)
    
    elif choice == 3:
        
        n = int (input("enter the number of elements to be appended: "))
        list1 = []
        for i in range(0,n):
            element = int(input("enter the element No - {} : ".format(i+1)))
            list1.append(element)
        demoList.extend(list1)

    elif choice == 4:

        pos = int (input("enter the position to be modified: "))
        n = int (input("enter the new element: "))
        demoList[pos] = n

    elif choice == 5:

        pos = int (input("enter the position to be deleted: "))
        del demoList[pos]

    elif choice == 6:

        n = int (input("enter the element to be deleted: "))
        demoList.remove(n)
    
    elif choice == 7:

        demoList.sort()
    
        print(demoList)
    elif choice == 8:

        demoList.sort(reverse = True)

        print(demoList)

    elif choice == 9:

        print(demoList)
    
    elif choice == 10:
        break

    else:
        print("invalid choice")

