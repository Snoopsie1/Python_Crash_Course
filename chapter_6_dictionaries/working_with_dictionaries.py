#Consider af game featuring aliens that can have different colors and point values.
# This simple dictionary stores information about a particular alien:
alien_0 = {"color": "green", "points" : 5}
print(alien_0["color"])
print(alien_0["points"])

#So what is a dictionary?
# A dictionary is a collection of key-to-value pairs.
# Each key is connected to a value.
# You can use a key to access a value associated with said key.
# A key's value can be a number, a string, a list or even another dictionary.
# Or any other ordinary object that you can create in Python.

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

