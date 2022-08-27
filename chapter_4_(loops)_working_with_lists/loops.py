#Time to mess with loops.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

#remember naming conventions doing for loops.
# for example:
# for dog in dogs
# for item in list_of_items
# etc.

for magician in magicians:
    print(f"{magician.title()}, that was great trick!")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you everyone, that was a great magic show!")