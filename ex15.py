# -*- coding: utf-8 -*-

from sys import argv
# script = py file name that I want to run
# filename =  the txt or word or whichever other file type
# i want to read the information from
script, filename = argv
# command that calls the content of the file as txt
txt = open(filename)

print "Here's your file %r:" % filename
# commands to read the txt
print txt.read()


# alternative way to get the same result
print "Type the filename again:"
# let's you input the file name and defines that as file_again
file_again = raw_input("Write here: ")

# command that calls the content of the file as txt
txt_again = open(file_again)
# commands to read the txt
print txt_again.read()

# the only difference between the two is writing the file name
# in the terminal directly or asking for an input