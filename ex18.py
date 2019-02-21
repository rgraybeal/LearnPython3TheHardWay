"""
Names, variables, Code, Functions

Functions do three things:
    1. they name pieces of code the wway variables name strings and numbers
    2. They take arguments the way your scripts take argv
    3. Using 1 and 2, they let you make your own mini-scripts" or "tiny-commands"

Making 4 functions:

"""

# this one is like your scripts with argv
def print_two(*args):
    for arg in args:
        print("input: ", arg)
    #arg1, arg2, arg3, arg4, arg5 = args
    #print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}, arg5: {arg5}")

# ok, that * args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Amelia", "Graybeal", "and", "five", "more")
print_two_again("Jillian", "Graybeal")
print_one("First!")
print_none()
