number = int(input("Enter an number:"))
is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % 2 == 0):
#             is_prime = False
#             print(number,"is not a prime number")
#             break
#     else:
#         print(number,"is a prime number")

if number > 1:
    if number % number != 0 :
        is_prime = False
        print(number, "is a not prime number")
    else:
        print(number, "is a prime number")