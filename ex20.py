# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv
# this is the function to open a file and read from it
# the stuff in the brackets is called "arguments", in this case "f"
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

# has two arguments	
def print_a_line(line_count, f):
	print line_count, f.readline(),
	
current_file = open(input_file)

print "First let's print the whole file:\n"
# this command runs the function
# in the brackets are values that I want to run, 
# could be more than one
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
