
def demoCal( n , demo_dict):

    demostr = ""

    for i in n :

        i = int(i)

        demostr += demo_dict[i] + " "

    return demostr

    
n = input()

demo_dict = {1:"one" , 2:"two" , 3:"three" , 4:"four" , 5:"five" , 6:"six" , 7:"seven" , 8:"eight" , 9:"nine" , 0:"zero"}

result = demoCal( n , demo_dict )

print(result)
