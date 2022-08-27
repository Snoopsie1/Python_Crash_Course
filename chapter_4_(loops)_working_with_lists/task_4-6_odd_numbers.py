#Use the third argument of the range() function to make a list of odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_numbers = [value for value in range(1, 20, 2)]

for odd_number in odd_numbers:
    print(odd_number)