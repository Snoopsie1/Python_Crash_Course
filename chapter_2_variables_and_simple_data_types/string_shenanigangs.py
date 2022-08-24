#Time to mess with some Strings!

name = "ada lovelace"
print(name.title())
#.title will print the name in title case. Where each word begins with a capital letter
#Output: Ada Lovelace
print(name.lower())
#Prints in lower case
#Output: ada lovelace
print(name.upper())
#Prints in upper case
#Output: ADA LOVELACE

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#This is an f-string.
#It's a string variable that contains other strings, formatted into it's value
message = f"Hello, {full_name.title()}!"
print(message)
#The "f" in the start of the "" in the f-strings value stands for FORMAT.
#It's so it knows how to construct, structure and store the string values it's given.

#f-strings were introduced in Python 3.6.
#If a system uses 3.5 or lower, it is recommended to use the format() syntax instead.

