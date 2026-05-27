
def change(list2):

    for i in range(0,len(list2)):

        list2[i] += 5
    
    print(list2 , id(list2))

list1 =[1,2,3,4,5]

print(list1 , id(list1))

change(list1)

print(list1 , id(list1))

