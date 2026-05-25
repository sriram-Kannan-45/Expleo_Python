def calculation(rate , salary):

    cal_rate = 0 ;
    if rate >=1 and rate <=4 :
        cal_rate = salary * 0.1
    elif rate > 4 and rate <= 7 :
        cal_rate = salary * 0.25
    elif rate > 7 and rate <= 10 :
        cal_rate = salary * 0.3
    
    return cal_rate

salary = int(input("Enter your salary: "))
rate = int(input("Enter the rate: "))

if (rate < 1 or rate > 10) and salary <= 0 :
    print("Invalid input. Please enter a valid salary and hike percentage.")
else:
    print("Your updated amount is: ", calculation(rate , salary)+ salary)
