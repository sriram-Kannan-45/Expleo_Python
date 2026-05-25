def caluculate(salary , hike):
    new_salary = salary + (salary * hike / 100)
    return new_salary

salry = int(input("Enter your salary: "))

hike = int(input("Enter the hike percentage: "))

print("Your new salary is: ", caluculate(salry, hike))