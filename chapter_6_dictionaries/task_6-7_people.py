#Start with the program you wrote for Exercise 6-1.
# Make two new dictionaries representing different people,
# and store all three dictionaries in a list called "people"
# Loop through your list of people.
# As you loop through the list, print everything you know about each person.
person_0 = {
    "first_name": "nikolaj",
    "last_name": "osv",
    "age": "44",
    "city": "lyngby",
    }
person_1 = {
    "first_name": "kaj",
    "last_name": "thunder",
    "age": "29",
    "city": "hundige",
}
person_2 = {
    "first_name": "beetle",
    "last_name": "juice",
    "age": "36",
    "city": "compton",
}

people = [person_0, person_1, person_2]

for people in people:
    print("\nInformation about this person:")
    for info, value in people.items():
        print(f"{info.title()} : {value.title()}")