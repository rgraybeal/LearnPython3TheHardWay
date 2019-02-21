"""

Reading and writing files

close

Read

readline

truncate - empties the files
write ("stuff")

seek(0)

"""

#import the argv module
from sys import argv

#unpack the command line arguments (first will be the script name, second the
#name of the file by user)
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL -C (^C).")
print("If you do want that, hit RETURN.")
#if you type control c, program crashes, keyboard interrupt
input("?")

print("Opening the file...")
target = open(filename, 'w+')

#print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")
allines = []
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write('\n'+ line1 + '\n' + line2 + '\n' + line3)

target.close()

print("Now reopening the file...")
print("The file contains the following information:")
target_2=open(filename, 'r')
print(target_2.read())
target_2.close()
