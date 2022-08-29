#Making huge dictionary can be an eyesore if you make it in one line.
# Let's clean up your one-liner habit and show how you can make a big dictionary - in a clean way.
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")