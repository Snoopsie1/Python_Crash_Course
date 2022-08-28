#To copy a list, we make a slice that's the entire list.
# And place that onto another variable.

my_foods = ["pizza", "falafel", "banana cake"]
friend_foods = my_foods[:] #Omit 1st and 2nd index

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#To prove that we actually have two seperate lists here, we'll add a new food to each list.

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#So here is where my java brain wanders off
# Why not just set friend_foods = my_foods?
# This is what happens when you copy a list without using a slice:

my_games = ["gotcha force", "mario kart", "mario party"]
friend_games = my_games

print("\n My games:")
print(my_games)
print("\n Friend's games:")
print(friend_games)

my_games.append("super smash bros")
friend_games.append("hello kitty island adventure")

print("\n My games after append:")
print(my_games)
print("\n Friend's games after append:")
print(friend_games)

#The reason this happens is because. When you assign a new list to be equal to another list.
# Then it's not a new list. It's a reference to the previous one.
# Therefore, when you want to make a new copy of a list, and use them as seperate lists.
# Use slices:)

