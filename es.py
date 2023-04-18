# Program that reads in a text file and outputs the number of e's it contains.
# It should take the filename from an argument on the command line.
# Author: Clare Tubridy
# 28-03-2023

import sys                                  # allows to take command line argument

# The text filename is held in the second arguement, argv[1]
filename = sys.argv[1]

# Opens files without having to use the close() function
with open(filename, 'r') as f:
    e = f.read()                            # store content of the file in a variable
    count = e.count('e') + e.count('E')     # counts upper and lower case e

    print(f"The letter 'e' shows up {count} times")