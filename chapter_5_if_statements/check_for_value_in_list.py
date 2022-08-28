#Sometimes it can also be impotant to check if something is in a list.
# It's super simple with Python with the "in" operation
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings) #This will return True
print("pepperoni" in requested_toppings) #This will return False

#You can also check if something is missing from a list with the "not in" operation
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    