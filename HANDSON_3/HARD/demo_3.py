def maxi(*args):
    
    max_value = 0
    for num in args:
        if num >= max_value:
            max_value = num
    
    return max_value

numbers = [8,15,22,17,12]
print("The maximum number is: ", maxi(*numbers))