# filename: name.py
# date: 03-20-2020
# username: rybrock@
# name: Ryan Brockman
# description: Various string operations - Python crash course

# Changing case in a string
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

# Combining or concatenating strings
firstName = 'ada'
lastName = 'lovelace'
fullName = firstName + ' ' + lastName
print(fullName.title())
message = "Hello, " + fullName.title() + "!"
print(message)

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
