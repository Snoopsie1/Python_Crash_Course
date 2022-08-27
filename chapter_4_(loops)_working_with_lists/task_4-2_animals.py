#Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list,
# and then use a for loop to print out the name of each animal.

common_animals = ["giraffe", "dog", "capybara"]

for animal in common_animals:
    print(animal.title())

# - Modify your program to print a statement about each animal, such as "A dog would make a great pet"
for animal in common_animals:
    print(f"A {animal.title()} would make a great pet!")

# - Add a line at the end of your program stating what these animals have in common.
print("\nThe following animals: ")
for animal in common_animals:
    print(animal.title())
print("shares the characteristic of walking on four legs.")
