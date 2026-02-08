order_size = input("Enter your coffee size: ")
extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"
print("order: ", coffee)