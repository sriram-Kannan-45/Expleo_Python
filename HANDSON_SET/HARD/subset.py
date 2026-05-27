input_set = set()

while True :

    val = input()

    if val == "" :

        break

    input_set.add(int(val))

input_set = list(input_set)
   
result = []

target = int(input())

i = 0
j = len(input_set) - 1

while i<j :

    while i!=j :

        if input_set[i] + input_set[j] == target :

            inerSet  = {input_set[i] , input_set[j] }

            result.append(inerSet)

            j = j - 1
            
        else :

            j = j - 1

    i = i + 1

print(result)
         
            

    