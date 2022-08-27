#Make a list of then numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

nums = [value for value in range(1_000_001)]
print(min(nums))
print(max(nums))
print(sum(nums))

#holy #!?& that was fast.