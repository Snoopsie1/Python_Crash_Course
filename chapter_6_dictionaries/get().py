#Using keys in square brackets to retrieve the value you're interested
# in from a dictionary might cause one potential problem:
# If the key you ask for doesn't exist, you'll get an error.
#   Let's see what happens when you ask for the point value of an alien that doesn't have a point value set:
alien_0 = {
    "color": "green",
    "speed": "slow",
    }
#print(alien_0['points'])
#We will get a KeyError - Saying that, said key doesn't exist.

#We will learn more about errorhandling later.
# But for dictionaries you can use the get() method to set a default value
# that will be returned if the requested key doesn't exist.
# The get() method requires a key as a first argument.
# As a second optional argument, you can pass the value to be returned if the key doesn't exist:

point_value = alien_0.get("point", "No point value assigned")
print(point_value)

#If there's a chance the key you're asking for might not exist,
# consider using the get() method instead of the square bracket notation.

#Also, if you leave out the second argument in the get() method, and the key doesn't exist.
# Python will return the value None.
# None means "No value exists."
# This is not an error: It's a special value meant to indicate the absence of a value.
# Example:
alien_height = alien_0.get("height")
print(alien_height)
