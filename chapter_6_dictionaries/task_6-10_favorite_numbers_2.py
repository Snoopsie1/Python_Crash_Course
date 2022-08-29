#Modify your program from Exercise 6-2,
# so each person can have more than one favorite number.
# Then print each person's name along with their favorite numbers.
persons_fave_number = {
    "gunner": [42, 12, 3],
    "eigil": [63, 92, 77],
    "oliver": [14, 9, 3],
    "max": [9, 11, 22],
    "asta": [7, 4, 88],
}

for person, numbers in persons_fave_number.items():
    print(f"{person.title()}'s favorite numbers:")
    for number in numbers:
        print(f"\t{number}")