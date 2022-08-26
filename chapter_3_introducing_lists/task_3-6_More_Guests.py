#You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.

# - Start with your program from Exercise 3-4 or Exercise 3-5.
guest_list = ["hans michaelsen", "pasha rasoli", "bo burnham", "michael waddell"]
# Add a print() call to the end of your program informing people that you found a bigger dinner table.
print("Dear guests, it has come to my attention that IKEA has a sale on a bigger dinner table."
      "\nAs a result, the dinner event will be housing more guests.\nHope you can still make it"
      "\n-OR.")
# - Use insert() to add one new guests to the beginning of your list.
guest_list.insert(0,"bon sai")
print(f"{guest_list[0].title()}, has been added to the guest list!")
# - Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, "middle man")
print(f"{guest_list[2].title()}, has been added to the guest list!")
# - Use append() to add one new guest to the end of your list.
guest_list.append("mogens mogensen")
print(f"{guest_list[-1].title()}, has been added to the guest list!")
# - Print a new set of invitation messages, one for each person in your list.
print("Hi everyone, hope you can make it w/e")

