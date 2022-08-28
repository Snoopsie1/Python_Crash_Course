#Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except for 1, 2 and 3.

# · Store the numbers 1 through 9 in a list.
numbers = [value for value in range(1, 10)]
# · Loop through the list.
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")