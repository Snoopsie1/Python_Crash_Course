#working with .range()
for value in range(1,5):
    print(value)

#The .range() method is fairly simple to use.
# .range(x,y,z)
# x = start index
# y = end index (not included in count)
# z = steps to take
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#numbers squared
squares = []
for value in range(1, 11):
    square = value ** 2 #this takes a value and squares it, remember?
    squares.append(square)

print(squares)

#This snippet of code can be done cleaner by doing the append in one line like:
clean_squares = []
for value in range(1, 11):
    clean_squares.append(value ** 2)

print(clean_squares)

#There exists also a few numerical functions in python to help you with numerical lists.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#The functions are:
# min(list)
print(min(digits))
# max(list)
print(max(digits))
# sum(list)
print(sum(digits))

#List comprehensions
# Generating a list in just one line of code.
# This takes the method we used earlier to generate our squares list, by doing a one-liner instead of four.
cleaner_squares = [value ** 2 for value in range(1, 11)]
print(cleaner_squares)