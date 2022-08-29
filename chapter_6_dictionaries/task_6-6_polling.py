#Use the code in favorite_languages.py
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }
# · Make a list of people who should take the favorite languages poll.
#   Include some names that are already in the dictionary and some that are not.
should_take_poll = ["connor", "sarah", "edward", "bean"]
# · Loop through the list of people who should take the poll.
#   If they have already taken the poll, print a message thanking them for responding.
#   If they have not yet taken the poll, print a message inviting them to take the poll.
for name in should_take_poll:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for responding")
    else:
        print(f"{name.title()}, please come take the poll")