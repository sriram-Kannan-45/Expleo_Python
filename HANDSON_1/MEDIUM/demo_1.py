weight = float(input("Weight :"))
height = float(input("Height :"))

if height > 0  and weight > 0:
    bmi = weight / (height ** 2)
    print("BMI :", f"{bmi:.2f}")
else:
    print("Height and weight must be positive values.")