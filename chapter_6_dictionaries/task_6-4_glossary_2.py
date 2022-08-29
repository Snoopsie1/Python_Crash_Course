#Now that you know how to loop through a dictionary, clean up the code in 6-3
# Use a loop to print the dictionary's keys and values instead of 500 prints.
glossary = {
    "loop": "automate a repetitive task",
    "list": "store multiple things",
    "elif": "beautiful conditional chains/blocks",
    "pop()": "removing and using said removed item",
    "slicing": "taking part of a list, or copying an entire list with slicing",
    "every-other slicing": "the weird syntax for printing every-other thing on a sliced-list: list[::2]"
    }

glossary["set"] = "a collection of unique items"
glossary["keys"] = "pointers to a value in a dictionary"
glossary["value"] = "value to a key in a dictionary"
glossary["none"] = "a return value, if no value exists"
glossary["del"] = "deletes items"

for term, definition in glossary.items():
    print(f"{term.title()}: \n{definition.title()}\n")

#When the loop works, add 5 more Python terms and values

