print("Python")
#Output: Python
print("\tPython")
#Output:    Python
# \t adds a tab to your text
print("Languages:\nPython\nC\nJavaScript")
#Output: Langauges:
#        Python
#        C
#        JavaScript
# \n adds a newline to your text

#Stripping whitespace
#Sometimes, a user can accidentally enter an input with whitespace.
#It looks the same for a user or any other human.
#But it's still vastly different data-strings for your system.
#Here's how to get rid of it.
favorite_language = 'python '
print(favorite_language)
#Output: python (with extra space on the end)
print(favorite_language.rstrip())
#Output: python (no extra space on the end)

#Strips the whitespace off of the variable permanently
favorite_language = favorite_language.rstrip()
print(favorite_language)

#However, rstrip only removes whitespace from the right side of the string.
#To remove whitespace from the left side of the string we use lstrip()

favorite_language = " python "
#Now we have whitespace on left and right side
favorite_language = favorite_language.rstrip()
#Strips on the right side
print(favorite_language)
favorite_language = favorite_language.lstrip()
#Strips on the left side
print(favorite_language)
