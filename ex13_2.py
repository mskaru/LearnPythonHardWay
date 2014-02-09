# -*- coding: utf-8 -*-

from sys import argv

zero, first, second = argv

print "The script is called: ", zero
print "Your first variable is: ", first
print "Your second variable is: ", second

age = int(raw_input("How old are you? "))
height = int(raw_input("How tall are you? "))

print "So you're %r old and %r tall." % (age, height)


