with open("text.txt" , "r+") as file :

    print ("starting tell - " , file.tell())

    content = file.read()

    print(content)

    print ("after the file read the tell - ", file.tell())

    print("first seek - " , file.seek(20))

    print("tell - ",file.tell())

    new_content = file.read()

    print(new_content)