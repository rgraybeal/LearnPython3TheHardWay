"""

More Practice Exercies 24


"""

print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("------------------")
print(poem)
print("------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}") #print the variable called five in an f"" statement

def secret_formula(started):
    # take input called started and return calculation
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    #Returns the values applied to three variables

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#take value in startpoint, call the secret_formula function, do the calculations and apply the output of the function to three variables - they could be any name - not the name of jelly_beans becomes beans.

# Remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It is just like with an f"" string
print(f"We'd have {beans}, beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an aasy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
