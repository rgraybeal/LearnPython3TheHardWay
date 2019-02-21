
"""
More Files
script to copy one file to another

"""

from sys import argv

script, from_file, to_file = argv

#indata = open(from_file).read()

#with open(to_file, 'w') as out_file:
#    out_file.write(indata


open(to_file, 'w').write(open(from_file).read())
