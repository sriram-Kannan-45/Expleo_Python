products = (input("Enter a list of product names separated by commas: "))

prodcts_list = products.split(",")

print ("List of Products:")
for product in prodcts_list:
    print(product)