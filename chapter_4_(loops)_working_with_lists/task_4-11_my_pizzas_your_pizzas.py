#Start with your program from exercise 4-1.
pizzas = ["hawaii", "pepperoni", "salad pizza"]
# Make a copy of the list of pizzas, and call it friend_pizzas
friend_pizzas = pizzas[:]

# · Add a new pizza to the original list.
pizzas.append("potato")
# · Add a different pizza to the list "friend_pizzas".
friend_pizzas.append("shrimp")
# · Prove that you have two separate lists.
#   Print the message "My favorite pizzas are:", and then use a for loop to print the first list.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
#   Print the message "My friend's favorite pizzas are:", and then use a for loop to print the second list.
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

