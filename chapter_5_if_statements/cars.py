cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
#This conditional example uses equality checks like "=="
# Here is more examples of equality-checks with ==
car = "bmw"
print("\nDear Python program, does my car variable equal to a 'bmw'?")
print(car == "bmw")

print("\nDear Python program, does my car variable equal to an 'audi'?")
print(car == "audi")

#Sometimes when you check for equality, you just want to check if it's the same word.
# And not if it's the same word, WITH the same capitalization and so on.
print("\nEqaulity, check methods")
car = "Audi"
print(f"does Audi == audi? [{car == 'audi'}]") #should give false, because of the little "a"
print(f"does Audi.lower() == audi? [{car.lower() == 'audi'}]\n")

#We can also check for inequality with the "!=" operation.
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")