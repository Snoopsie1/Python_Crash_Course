#We've worked with single elements in a list, and entire lists.
# Time to work with pieces of a list:)

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])

#normally you'd via a single index. Like 1, 4 or -1.
# to get a slice of the list we give the list 2 parameters.
# a start index, a ":", and an end index.

#sum it up:
#get one from list
#players[x]
#get slice from list
#players[x:y]

#however, if you leave the first index-parameter empty, Python will automatically start your slice at the start
print(players[:4])
#same thing works if you leave the second index-parameter empty
print(players[2:])

#and if you want to get extra fancy. You can use the negative index (-x)
# to get for example, the last three players in a list
print(players[-3:])

#you can also add a third parameter when slicing.
# the third parameter indicates how many items to skip between items in the specified range
# just like the range(x,y,z) method.
print(players[::2])
# This looks total fucking alien to a java programmer. But this basically says to Python
# "Print every second player in the players list"