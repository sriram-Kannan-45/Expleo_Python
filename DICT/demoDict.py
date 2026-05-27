My_dict = {}

print(type(My_dict))

My_dict_2 = {1:"CSE" , "name" : "sriram" , "list" : [123,1,3] , "tuple" : (1,2)}

print(type(My_dict_2['list']))

My_dict_3 = dict(a=10,b=20)

print(My_dict_3 , type (My_dict_3))

My_dict_4 = dict({'a':1,'b':2})

print(My_dict_4 , type (My_dict_4))

print(My_dict_4['a'])

this_dict = {"brand" : "Ford" , "model" : "chatgpt"}

this_dict["name"] = "Sriram"

print(this_dict)

for i in this_dict:

    print(i)

print(this_dict.keys() , this_dict.values() )

this_dict.pop("brand")

print(this_dict)

demo_dict = {1:"one" , 2:"two"}

demo_dict.update({2:"three" , 3 :"to"})

print(demo_dict)