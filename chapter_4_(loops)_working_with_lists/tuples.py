#List of items that cannot change are called Tuples.
# They are what you call for "Immutable Lists"
# Bon appétit.

#A Tuple looks just like a list except you use a parentheses
# instead of square brackets when defining them.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#You can access data in a tuple just like you can in a normal list.

#dimensions[0] = 250
#That line of code will raise an error, because you cannot change what is on the tuple.

#Sidenote about Tuple:
# Tuples are technically defined by the presence of a comma;
# the parentheses make them look neater and more readable
# If you want to define a tuple with one element, you need to include a trailing comman:
my_t = (3,)
#It doesn't often make sense to build a tuple with one element,
# but this can happen when tuples are generated automatically

#You loop through a tuple the same way you do with a list.
print("\nLOOP TIME")
for dimension in dimensions:
    print(dimension)
