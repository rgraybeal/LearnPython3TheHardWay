"""
Functions and files

remembering the function checklist, using functions and files together to
make magic

"""
# get the argv module from sys
from sys import argv

# unpack the terminal arguments: script(implicit), file(explicit)
script, input_file = argv

# print the contents of a file
# where is the passing of the argument to f?
def print_all(f):
    print("First let's print the whole file:\n")
    print(f.read())

# set cursor to beginning of file
def rewind(f):
    print("Now let's rewind, kind of like a tape.")
    f.seek(41 +47 + 41)
# print the first line and return a number of lines
#takes two arguments, line count and file
def print_a_line(line_count, f):
    print(line_count, f.readline(), "Line length:", len(f.readline()))
    #print("Line length:", len(f.readline()))
    #print(len(f.readline()))

# set variable to terminal input
current_file = open(input_file)


print_all(current_file)


# call the rewind function with the file in use
rewind(current_file)

print("Let's print three lines:")

# set a counter to 1, initialize the variable
current_line = 1

# call function and pass two arguments
# current line doesn't inform which line is being read, just makes for nice
#formatting. Readline reads the next line in the file.
print_a_line(current_line, current_file)

#simply adds a number to the formatting, reads the next line
current_line += 1
print_a_line(current_line, current_file)


current_line +=1
print_a_line(current_line, current_file)

print("\n")
