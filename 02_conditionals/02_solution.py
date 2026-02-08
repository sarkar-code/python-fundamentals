age = int(input("Enter your age:"))

day = input("Enter your day:")

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2 #price -= 2

print(f"Ticket price for age {age} is {price}")