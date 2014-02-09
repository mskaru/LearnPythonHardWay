# -*- coding: utf-8 -*-

from sys import argv
# Note that the next line: script = the name of this exercise file
# the user_name means whatever name I give when running the command:
# for example: python ex14.py kris
script, user_name, age = argv
prompt = 'Write here: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions, inlcuding about your %r." % age
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How old are you?"
years = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. 
And you are %r years old. Nice.
""" % (likes, lives, computer, years)