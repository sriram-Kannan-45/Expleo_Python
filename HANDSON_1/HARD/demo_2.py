price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))

if price < 0 or quantity < 0:
    print("Price and quantity must be non-negative.")
else:
    total_cost = price * quantity
    print("Total cost: $", f"{total_cost:.2f}")
