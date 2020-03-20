# filename: stripping_names.py
# date: 03-20-2020
# username: rybrock@
# name: Ryan Brockman
# description: Python crash course - Chapter 2 - Exercise 2-7 - Stripping names

# Store a person's name, and include some whitespace chars at the beginning and end
# Print the name once, so whitespace is displayed. Then print using the three stripping functions.

# Adding whitespace to strings
# Tabs
print("Python rocks!")
print("\tPython rocks!")
# Newline
print("Languages: \nPython\nC\nJavascript")
print("Languages: \n\tPython\n\tC\n\tJavascript")

# Stripping whitespace
# Strip right and left individually
favoriteLanguage = ' python '
print('X' + favoriteLanguage + 'X')
favoriteLanguage = favoriteLanguage.rstrip()
favoriteLanguage = favoriteLanguage.lstrip()
print('X' + favoriteLanguage + 'X')

# Strip right and left with a single command
favoriteLanguage = ' python '
print('X' + favoriteLanguage + 'X')
favoriteLanguage = favoriteLanguage.strip()
print('X' + favoriteLanguage + 'X')
