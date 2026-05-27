try :

    fh = open("path/text.txt" , "w")

    try:

        fh.write ("this is sriram")
    finally :

        print("Going to close ")
        fh.close()
    
except IOError :

    print("io error")

else :

    print("iam else")

finally :

    print("iam alwasys run")