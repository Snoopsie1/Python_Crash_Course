#We can also compare numbers!
age = 17
print(age == 18)

#Or make silly checks
answer = 17 #Imagine this was an input from a game
#And if it wasn't the right answer this was the output:
if answer != 42:
    print("That is not the correct answer. Please try again!")

print("\nTesting other conditions")
#We can also do:
# > (bigger than),
print(age > 21)
# >= (bigger than or equal to),
print(age >= 18)
# < (less than),
print(age < 20)
# <= (less than or equal to)
print(age <= 20)

#We can also do cool stuff like checking for multiple thing in one line, with the "and" operation
print(f"Am I old enough to buy alcohol and learn to drive in Denmark?: {age >= 16 and age >= 18}")
#We can also check for either or, with "or" operation.
print(f"Respond with True if I am old enough to buy liquor or drive in Denmark: {age >= 16 or age >=18}")