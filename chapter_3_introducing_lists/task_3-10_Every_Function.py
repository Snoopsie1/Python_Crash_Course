#Think of something you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, language or anything you'd like.
# Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.
cryptids = ["squonk", "mothman", "loveland frogman", "snipe", "metal man of alabama", "big foot", "chessie"]

#selecting an element of our list
print(f"\n{cryptids[0].title()} is my favorite cryptid")

#adding an element to the end of our list
cryptids.append("dingbelle")
print(f"\n{cryptids[-1].title()} has been added!")

#adding an element to an indexed spot on our list
cryptids.insert(4, "quetzalcoatlus")
print(f"\n{cryptids[4].title()} has been added!")

#deleting by index
print(f"\nList before deletion: {cryptids}")
del cryptids[5]
print(f"List after deletion: {cryptids}")

#deleting by .pop()
print(f"\nList before pop: {cryptids}")
print(f"{cryptids.pop().title()} has been popped!")
print(f"List after pop: {cryptids}")

#deleting by indexed .pop(x)
print(f"\nList before pop: {cryptids}")
print(f"{cryptids.pop(5).title()} has been popped!")
print(f"List after pop: {cryptids}")

#removing elements by using .remove(string[] args)
print(f"\nList before removing by value: {cryptids}")
cryptids.remove("mothman")
print(f"List after removing by value: {cryptids}")

#permanently sorting a list alphabetically
print(f"\nUnsorted list: {cryptids}")
cryptids.sort()
print(f"Sorted list: {cryptids}")

#doing it in reverse
print(f"\nUnsorted list: {cryptids}")
cryptids.sort(reverse=True)
print(f"Sorted list: {cryptids}")

#temporarily sorting a list
print(f"\nUnsorted list: {cryptids}")
print(f"Sorted list: {sorted(cryptids)}")

#temporarily sorting a list in reverse
print(f"\nUnsorted list: {cryptids}")
print(f"Sorted list: {sorted(cryptids, reverse=True)}")

#Change the permanent order of a list to reverse
print(f"\nList before it got it's order reversed: {cryptids}")
cryptids.reverse()
print(f"List after it got it's order reversed: {cryptids}")

#find the length of a list
print(f"\nLength of my list of cryptids [{len(cryptids)}]")
print(cryptids)
