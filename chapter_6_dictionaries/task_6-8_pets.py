#Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.
#(So, same as 6-7)
pet_0 = {
    "type": "dog",
    "owner": "kaj",
}
pet_1 = {
    "type": "cat",
    "owner": "rosa",
}
pet_2 = {
    "type": "alpaca",
    "owner": "alberte",
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\nHere is some information about this pet:")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")