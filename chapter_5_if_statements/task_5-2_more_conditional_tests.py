#Time to do more tests!
# Have at least one True and one False result for each of the following:
# · Tests for equality and inequality with strings
name = "oliver"
print(f"Is my name Oliver?: [{name == 'oliver'}]")
print(f"My name is not Sebastian: [{name != 'sebastian'}]")
# · Tests using the lower() method
car = "BMW"
print(f"Is your car a BMW?: [{car.lower() == 'bmw'}]")
print(f"Is your car a BMW?: [{car.lower() == 'BMW'}]")
# · Numerical tests involving equality and inequality,
guess = 14
answer = 18
print(f"Is {guess} == {answer}?: [{guess == answer}]")
print(f"Is {guess} != {answer}?: [{guess != answer}]")
#   greater than
print(f"Is {guess} > {answer}?: [{guess > answer}]")
#   and less than,
print(f"Is {guess} < {answer}?: [{guess > answer}]")
#   greater than or equal to,
print(f"Is {guess} >= {answer}?: [{guess > answer}]")
#   and less than or equal to
print(f"Is {guess} <= {answer}?: [{guess > answer}]")
# · Tests using the "and" keyword and the "or" keyword
mom_age = 56
dad_age = 59
my_age = 24
print(f"Am I older than my mom and dad?: [{my_age > mom_age and my_age > dad_age}]")
print(f"Am I older than my mom or dad?: [{my_age > mom_age or my_age > dad_age}]")
# · Test whether an item is in a list
my_pocket = ["keys", "phone", "airpods"]
print(f"Did i remember my wallet?: [{'wallet' in my_pocket}]")
# · Test whether an item is not in a list
print(f"I remembered to leave my toothbrush at home, right?: [{'toothbrush' not in my_pocket}]")
