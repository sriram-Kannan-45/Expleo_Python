my_tuple_1 = 10

print(type(my_tuple_1))

my_tuple_2 = 1 , 

print(type(my_tuple_2
           ))

my_tuple_3 = (1,2.1,"sriram",[0,2,3])

print(type(my_tuple_3))
print(type(my_tuple_3[-1]))

t = (10,20,30,40,50)

t = (100,) + t[1:]

print(t)

addr = 'monthly@python.org'

uname,domain  = addr.split("@")

tup = uname , domain

print(type(tup))
print(uname ,"===", domain , type (uname) , type(domain))

q ,r = divmod(7,3) 
print(q) 
print (r)
