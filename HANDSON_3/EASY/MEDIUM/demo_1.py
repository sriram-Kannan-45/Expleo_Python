def sumOddEven (start , end):

    sum_odd = 0
    sum_even = 0

    for i in range (start , end+1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_odd , sum_even

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
odd_sum , even_sum = sumOddEven(start , end)
print("The sum of odd numbers is from ", start, " to ", end, "is :", odd_sum)
print("The sum of even numbers is from ", start, " to ", end, "is :", even_sum)
print("The absolute difference between the sums is :", abs(odd_sum - even_sum))

