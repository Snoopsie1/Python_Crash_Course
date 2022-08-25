#Lists is a 0-indexed list of items, it can be names, numbers etc.  Just like Java

bicycles = ["trek", "cannondale", "redline", "specialized"]
#This will print the entire list. Brackets and quotes included.
print(bicycles)
#This will print first element of the list.
print(bicycles[0])
#And this will print first element with capitalized letters.
print(bicycles[0].title())

#This will print the 2nd and 4th element of the list
print(bicycles[1])
print(bicycles[3])

#Python has a funny way of accessing the last way of a list.
print(bicycles[-1])
#Apparently this will ALWAYS return the last item of a list.
#Might be handy.

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
