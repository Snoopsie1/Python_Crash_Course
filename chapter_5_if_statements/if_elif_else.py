#Sometimes we wanna check for more than If or Else
# What if there is more than 2 potential outcomes?
# This is where elif steps in.
age = 12
if age < 4:
    print("Your admission cost is $0.")
#checks if the person is under 4 years old.
elif age < 18:
    print("Your admission cost is $25.")
#checks if the person is under 18, it only runs if the first test fails
# so actually, it checks if age is between 4 and 18.
else:
    print("Your admission cost is $40.")
#final check for if the person is over 18 years old.

#This code can be done way cleaner tho.
# check this shizzle out.

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#Sometimes there can be more elifs in an elif-block

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

#Sometimes we don't need an else at the end of an elif-block.
# It's a good catchall method, but not necessary in most cases,
# if you can catch all outcomes before the end of the block

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
