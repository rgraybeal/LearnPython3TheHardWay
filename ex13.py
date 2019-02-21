"""
Paraments, Unpacking and Variables
1/10/18, on call
Randy R. Graybeal

passing argv  in the terminal

"""

from sys import argv
#read the WYSS section for how to run this
#ARGV = argument variable - holds arguements you pass to the script
# #unpacks variable into four variables
#you can work with
try:
    script, first, second, third = argv
    user_input = input("What input do you have?: ")
    print("The script is called: ", script)
    print("Your first variable is: ", first)
    print("Your second variable is: ", second)
    print("Your third variable is: ", third)
    print(f"You typed {user_input}")
except ValueError:
    print("You forgot to add the right number of arguments in terminal")
