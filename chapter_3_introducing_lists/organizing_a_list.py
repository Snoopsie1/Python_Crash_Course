#To permanently organize a list alphabetically we can use .sort()
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
#And to do it in reverse we use this argument in the method
cars.sort(reverse=True)
print(cars)

#To temporarily sort a list we use the sorted(list) method call
veteran_cars = ["toyota", "suzuki", "ferrari", "mitsubishi"]
print("Here is the original list:")
print(veteran_cars)
print("\nHere is the sorted list:")
print(sorted(veteran_cars))
print("\nHere is the original list again:")
print(veteran_cars)

#sorted can also use reverse=True arguments
print("\nHere is the sorted list in reverse:")
print(sorted(veteran_cars, reverse=True))

#To reverse the original order of a list. You can use the .reverse() method.
champions = ["ryze", "aatrox", "sett", "udyr", "tristana", "gnar"]
print(f"\n{champions}")
champions.reverse()
print(f"\n{champions}")
#It changes the order of the list permanently. But you can revert it back anytime by using .reverse() again.

#Find the length of a List.
#To find the length of a list. We use the method .len(list)

forgotten_champions = ["ryze", "aurelion sol", "maokai"]
print(len(forgotten_champions))
