# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
	print "A room is full of gold. How much do you take?"
	
	# this part is checking that what you enter is a number not a word
	next = raw_input("> ")
	how_much = int(next)
	
	#Alternative way to avoid the person inputting non-numbers:
	#if "0" in next or "1" in next:
		#how_much = int(next)
	#else:
		#dead("Man, learn to type a number")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door.!"
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and kills you")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"
			

def chu_room():
	print "Here you see the evil Chu"
	print "He startes at you and you go insane"
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		chu_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room"
	print "There is a door to your right, left and straight"
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "straight":
		bear_room()
	elif next == "right":
		chu_room()
	elif next == "left":
		gold_room()
	else:
		dead("You stumble around the room until you starve")
		
start()