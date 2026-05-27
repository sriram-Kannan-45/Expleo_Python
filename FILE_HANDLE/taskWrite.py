with open("text.txt", "a") as demoFile:

    previous = ""

    while True:

        txt = input()

        if txt == "" and pre == "":
            break

        demoFile.write(txt + "\n")

        pre = txt