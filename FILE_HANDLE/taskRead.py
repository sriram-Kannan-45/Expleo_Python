with open ("text.txt" , "r") as demoFile:
     
     content = demoFile.readlines()

     for txt in content :
          
          print(txt , end="")
