#You just found out that your new dinner table won't arrive in time for the dinner,
# and you have space for only two guests!

# - Start with your program from Exercise 3-6.
guest_list = ["hans michaelsen", "pasha rasoli", "bo burnham", "michael waddell"]
guest_list.insert(0,"bon sai")
guest_list.insert(2, "middle man")
guest_list.append("mogens mogensen")
#   Add a new line that prints a message saying that you can invite only two people for dinner
print("To all my dear invited guests. It has come to my attention that my table can only host extra people"
      "\nI am very sorry for the inconvenience, but I have to resort to decline some of the invitations that were handed out."
      "\nSorry\n-OR")
# - Use pop() to remove guests from your list one at a time until only two names remain in your list.
#   print a message to that person letting them know you're sorry you can't invite them to dinner.
print("- - - - List before popping - - - -")
print(guest_list)
print(f"Sorry, {guest_list.pop().title()}, I sadly have to take back my invitation that I gave you.")
print(f"Sorry, {guest_list.pop().title()}, I sadly have to take back my invitation that I gave you.")
print(f"Sorry, {guest_list.pop().title()}, I sadly have to take back my invitation that I gave you.")
print(f"Sorry, {guest_list.pop().title()}, I sadly have to take back my invitation that I gave you.")
print(f"Sorry, {guest_list.pop().title()}, I sadly have to take back my invitation that I gave you.")
print("- - - - List after popping - - - -")
print(guest_list)
# - Print a message to each of the two people still on your list, letting them know they're still invited.
print(f"Hi {guest_list[0].title()} and {guest_list[1].title()}, hope to still see you at dinner.")
# - Use del to remove the last two names from your list, so you have an empty list.
del guest_list[-1]
del guest_list[-1]
#   Print your list to make sure you actually have an empty list at the end of your program.
print((guest_list))