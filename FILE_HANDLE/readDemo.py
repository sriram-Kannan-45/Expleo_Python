with open ("text.txt" , "r") as file :

    # var = file.read(-1)

    # var = file.readline()

    var = file.readlines()

    for line in var :

        # words = line.split()

        words = line.splitlines()
        
        print(words)

    print(var)