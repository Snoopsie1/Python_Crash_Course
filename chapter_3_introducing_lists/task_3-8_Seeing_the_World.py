#Think of at least five places in the world you'd like to visit.
# - Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ["tokyo", "hawaii", "seoul", "portugal", "greece", "rome"]

# - Print your list in its original order.
#   Don't worry about printing the list neatly, just print it as a raw Python list.
print(locations)

# - Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(locations))

# - Show that your list is still in its original order by printing it again.
print(locations)

# - Use reverse() to change the order of your list. Print the list to show its order has changed
locations.reverse()
print(locations)

# - Use reverse() to change the order of your list. Print the list to show it's back to its original order.
locations.reverse()
print(locations)

# - Use sort() to change your list, so it's stored in alphabetical order.
#   Print the list to show that its order has been changed.
locations.sort()
print(locations)

# - Use sort() to change your list, so it's stored in reverse alphabetical order.
#   Print the list to show that its order has changed.
locations.sort(reverse=True)
print(locations)
