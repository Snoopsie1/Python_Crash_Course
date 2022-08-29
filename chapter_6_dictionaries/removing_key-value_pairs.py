#When you no longer need a piece of information that's stored in a dictionary,
# you can use del statements to completely remove a key-value pair
# All the del statement needs is the name of the dictionary and it's key.
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)