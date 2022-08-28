#Make a list of five or more usernames, including the name "admin".
usernames = ["gunner", "snoopsie", "bean", "adabab", "admin"]
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user:
for username in usernames:
# · If the username is "admin", print a special greeting such as
#   "Hello Admin, would you like to see a status report?"
    if username == "admin":
        print(f"Hello {username.title()}, would you like to see a status report?")
# · Otherwise, print a generic greeting such as "Hello Jaden, thank you for logging in again."
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")