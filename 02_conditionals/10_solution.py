pet_species = input("Enter your pet species:")
age = int(input("Enter your pet's age:"))

if pet_species == "Dog":
    if age < 2:
        food_type = "Puppy food"
    else:
        food_type = "Not known"

if pet_species == "Cat":
    if age < 5:
        food_type = "Senior cat food"
    else:
        food_type = "Not known"

print(food_type)