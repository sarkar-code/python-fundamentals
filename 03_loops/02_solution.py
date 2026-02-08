n = int(input("Enter an number:"))
sum_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
print(f"Sum of even numbers upto {n} is :", sum_even)