#A single Python dictionary can contain mountains of information,
# No sane individual would manually print, access or modify individual data one-by-one
# It's too repetitive.
# So here's how to do it with loops!

#Looping through all key-value pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
    }
for key, value in user_0.items():
    print(f"\nKey {key}")
    print(f"Value {value}")

#What we are telling Python is:
# For every key-value in dictionary.items(): print("whatever")
# dictionary.items() returns a list of key-value pairs.

#The proper syntax for a for-each loop with dictionary is:
# for key, value in dictionary.items():
# As a developer you declare variable names for key and value in the for-each statement.
# It can be called whatever you want. As long as it makes sense to you and makes the code readable
#Another example:
print("\n")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#You can also just loop through all the keys in a dictionary.
print("\nWith .keys()")
for name in favorite_languages.keys():
    print(name.title())
#dictionary.keys() returns a list of keys from said dictionary.
# Here is the proper syntax:
# for key in dictionary.keys():

#However, looping through the keys is actually the default behavior when looping through a dictionary,
# so this code would have exactly the same output if you wrote...
print("\nWithout .keys()")
for name in favorite_languages:
    print(name.title())
#So if you want, you can omit .keys()
# And only use .keys() for readability’s sake
print("\ncontainment conditionals")
friends = ["edward", "phil"]

if "erin" not in favorite_languages.keys(): #Checks if the erin key is there
    print("Erin, please tak our poll!")

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#We can also loop through a dictionary's key in a particular order
print("\nAlphabetically sorted dictionary' keys")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

#If we can get a list of keys and loop through that, we should be able to do the same, but with values.
# And yes we can.
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#This method pulls all values from a dictionary, even duplicates, since it's printed as a list.
# If we were dealing with a large dictionary, with many duplicate values, it could be a waste of output.
# To circumvent this, we can make the list into a set.
# A set is a collection, in which each item must be unique:
print("\n The following languages have been mentioned:")
for langauge in set(favorite_languages.values()):
    print(langauge.title())
# What did we do different?
# We said to Python: for every value in the set, made from the list of values from the dictionary, do this.
# If we wrap set() around a list with duplicate items,
# Python identifies the unique items in the list and builds a set from those items.

#If you want to build a set directly you can do it so:
#SET
langauges = {"python", "ruby", "python", "c"}
print(langauges)
#And here is the same variable as a list, to show the difference:
#LIST
langauges = ["python", "ruby", "python", "c"]
print(langauges)