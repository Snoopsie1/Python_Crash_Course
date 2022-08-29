#Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary.
# For example, consider how you might describe a pizza that someone is ordering.
# If you were to use only a list, all you could really store is a list of the pizza's toppings.
# With a dictionary, a list of toppings can be just one aspect of the pizza you're describing:

#Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
    }
#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
      " with the following toppings: ")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

#We can do the same example as with favorite languages
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")