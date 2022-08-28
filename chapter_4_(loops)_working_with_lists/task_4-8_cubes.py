# A number raised to the third power is called a cube.
# For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube.

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

#Proof
print("- - - - - Buffer - - - - -")
print(1**3)
print(2**3)
print(3**3)
print(4**3)
print(5**3)
print(6**3)
print(7**3)
print(8**3)
print(9**3)
print(10**3)