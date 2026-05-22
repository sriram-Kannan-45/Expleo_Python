mark = int(input("Enter your mark: "))

if mark > 90:
    print("Grade: O")
elif mark <=90 and mark >=81 :
    print("Grade: A")
elif mark <=80 and mark >=71 :
    print("Grade: B")
elif mark <=70 and mark >=61 :
    print("Grade: C")
elif mark <=60 and mark >=50 :
    print("Grade: D")
else:
    print("Grade: F")