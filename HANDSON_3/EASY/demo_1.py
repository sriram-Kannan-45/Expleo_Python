def sumOddEven(numbers):
    oddSum = 0
    evenSum = 0
    for i in numbers:
        if i % 2 == 0:
            evenSum = evenSum + i
        else:
            oddSum = oddSum + i
    return oddSum, evenSum
numbers = [1,2,3,4,5,6,7,8,9]
oddSum, evenSum = sumOddEven(numbers)
print("the sum of odd numbers is : ", oddSum)
print("the sum of even numbers is : ", evenSum)
