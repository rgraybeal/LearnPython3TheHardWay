"""
Reading files
1/10/19


use ex15_sample.txt

don't hardcode the filename into the code, take argv or user input

"""
#import the argv functions from the sys module
from sys import argv

#unpack the [0] and [1] parameters from the terminal
script, filename = argv

#open the file and put it to the txt variable
txt = open(filename)

#print the name of the file
print(f"Here's your file {filename}:")
#read the file and print its contents
print(txt.read())
txt.close()

#take input from the user from within the program
print("Type the filename again: ")
file_again = input("> ")

# put contents of file to txt_again variable
txt_again = open(file_again)

# print out contents of file
print(txt_again.read())
txt.close()
