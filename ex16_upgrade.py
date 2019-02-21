
"""
Write a script like ex16 that uses read and argv to read the file you just
created

"""

from sys import argv

script, filename = argv

text = open(filename, 'r')
print("The contents of the file: ", filename, "is:")
print(text.read())
