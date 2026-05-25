Greet = "hi"
print(Greet)


# del Greet

# print(Greet)

print(len(Greet))

#traversing the string

#while loop

demo = "Hello World"
index = 0

while index < len(demo):

    print(demo[index])
    index += 1

#for loop
for i in demo:
    print(i )

#slicing of string

print(demo[-3:-1])

print(demo[0:5:-1])

str_1 = "Good Day"
print(str_1[::2])
print(str_1[::3])
print(str_1[::-1])
print(str_1[::-2])

#concatenation of string
str_2 = "Everyone"
print(str_1 + " " + str_2)
print(str_2*3)

#in

print("Day" in str_1)
print("day" in str_1)

demo_1 = "Hello, World!"
new_demo = "j"+demo_1[7:]
print(new_demo)
new_demo_1 = "j"+demo_1[-6:-1]
print(new_demo_1)


print(new_demo_1.upper())
print(new_demo_1.lower())
print(new_demo.find("o"))
print(demo.find("o", 1, 12))

new = demo_1.replace("Hello", "Hi")
print(new)

print(demo_1.count("o"))
print(demo_1.capitalize())

print(demo_1.startswith("Hello"))
print(demo_1.endswith("!"))
print(demo_1.isalnum())
print(demo_1.isalpha())
print(demo_1.isdigit())