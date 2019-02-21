"""

What was that?
1/6/18

escape characters

study drills:
1. memorize the escape sequences by putting them on flash cards
2. use \'\'\' instead. why use \"\"\" preferentially
3. combine escape and format strings to create a more complex format
"""

# assign a string to a variable, use the escaped tab
tabby_cat = "\tI'm tabbed in."
# string to variable, use new line in middle of string
persian_cat = "I'm split\non a line."
# string to variable, use backslash escaped
backslash_cat = "I'm \\ a \\ cat."

# assign a triple-quoted string to variable using tab and newlines,
# fancy formatting
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# print each of the variables
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# 3. combine escape and format strings to create a more complex format

wide_cat = """
\tVery wide cat\n\t\tis\n\n\t\t\t\tthis wide
"""

print(wide_cat)
