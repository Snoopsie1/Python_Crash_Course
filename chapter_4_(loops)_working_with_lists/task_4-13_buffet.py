#A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple
restaurant_menu = ("banana-split", "avocado sandwich", "coffee", "pizza-slice", "protein shake")
# · Use a for loop to print each food the restaurant offers.
print("Original restaurant menu:")
for item in restaurant_menu:
    print(item.title())
# · Try to modify one of the items, and make sure that Python rejects the change
#restaurant_menu[0] = "apple pie"
# · The restaurant changes its menu, replacing two of the items with different foods.
#   Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
restaurant_menu = ("apple pie", "avocado sandwich", "kovfefe", "pizza-slice", "protein shake")
print("\nModified restaurant menu:")
for item in restaurant_menu:
    print(item.title())
