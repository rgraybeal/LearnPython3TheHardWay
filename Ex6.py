"""
Strings and Text

f-string or
.format() syntax useful to apply to an already created string as in a loopself.

Study Drills:
1. Comment for each line
2. Find all the places (4) where a string is put inside a stringself.
3. Explain why adding two strings (W + e) makes a longer string.
"""

#setup variables
type_of_people = 10
#string in a string 1
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
#strings in a string 2 and 3
y = f"Those who know {binary} and those who {do_not}"

#output two strings containing strings
print(x)
print(y)

#output two more strings within strings (numbers 4 and 5)
print(f"I said: {x}")
print(f"I also said: '{y}'") #prints a quote around the output for y

#set variable to bolean value
hilarious = True
#string within a string 6. Variable takes a parameter
joke_evaluation = "Isn't that joke so funny?! {}"
#feed parameter to joke_evaluation variable
print(joke_evaluation.format(hilarious))

#two strings
w = "This is the left side of..."
e = "a string with a right side."

#concatenate two strings
print(w + e)
