#Time to mess with lists.
#Initial list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#Changing first element to something else
motorcycles[0] = "ducati"
print(motorcycles)

#ADD
#Instead of changing the element to something new, we can just add it instead.
#with .append(element)
motorcycles.append("honda")
print(motorcycles)

empty_garage = []
empty_garage.append("tesla")
empty_garage.append("hayabuza")
empty_garage.append("toyota")

print(empty_garage)

#INSERT
#We can also just insert stuff into specific places on our list
seats_at_table = ["jasmin", "thomas", "jonas", "laura"]
seats_at_table.insert(1,"jorg")
seats_at_table.insert(-1, "josefine")
print(seats_at_table)

#REMOVE by Index
#And if some element has to be removed
del seats_at_table[-1]
print(seats_at_table)

del seats_at_table[1]
print(seats_at_table)

#POP
#Sometimes you'll want to use the value of an item after you remove it from a list.
#For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion.
#Or remove a user from a list of active users and move that user to a list of inactive users.
#So why the word "Pop"?
#The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.
#In this analogy, the top of a stack corresponds to the end of a list.
#REMEMBER. When you pop(), the item is removed from said list.
people_at_the_party = ["Hanne", "Thomas", "Tobias", "Anders", "Dizzy"]
print(f"Damn this is a crazy party. everyone, including: {people_at_the_party}, is here")

popped_party_person = people_at_the_party.pop()
print(f"okay, the party was fine, but {popped_party_person} was a little too wild. So we removed him from the party")

#You can also pop items in any position of a list. Doesn't have to be the end of one.
popped_party_person = people_at_the_party.pop(0)
print(f"Okay okay okay, this is getting too crazy, {popped_party_person} caught fire in her hair and wrestled a bear.")
print(f"The only survivors of this party are {people_at_the_party}")

#REMOVE by Value
#If I don't know the index of a certain item I want to remove.
print(f"Someone have to get a hold of {people_at_the_party[-1]}, he is acting crazy")
people_at_the_party.remove("Anders")
print(f"Okay, he is gone now. Now we only have {people_at_the_party} left.")


