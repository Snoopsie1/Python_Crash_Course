#Sometimes it's nice to check for stuff in a list. Here are some examples:
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

#Nice example, but what if the pizza-parlor is out of green peppers?

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza\n")

#We can also check if a list is empty

weird_pizza_request = []

if weird_pizza_request: #If before a list call checks if there is an item in the list.
    for weird_pizza_toppings in weird_pizza_request:
        print(f"Adding {weird_pizza_toppings}")
    print("\nFinished making your pizza")
else: #Since there isn't it jumps directly down here
    print("Are you sure you want a plain pizza?")
