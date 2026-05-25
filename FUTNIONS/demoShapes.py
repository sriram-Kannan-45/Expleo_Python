def circule ( r ):

    print ("Area of the circle : ", 3.14*(r**2))

def squre (s):

    print ("Area of the squre : ",s*s)

def rectangle ( l , b) :

    print("Area of the Ractangel : " , l*b)

while True :

    print("1. Area of the circle")
    print("2. Area of the squre")
    print("3. Area of the rectangle")
    print("4. Exit")

    c = int(input("Enter the choice : "))


    if (c == 1) :
        r = int(input("Enter the radius of the circle : "))
        circule(r)
    elif (c == 2) :
        s = int(input("Enter the side of the squre : "))
        squre(s)
    elif (c == 3) :
        l = int(input("Enter the length of the rectangle : "))
        b = int(input("Enter the breadth of the rectangle : "))
        rectangle(l , b)
    elif (c == 4) :
        print("Exiting the program...")
        break
    else :
        print("Invalid choice. Please try again.")