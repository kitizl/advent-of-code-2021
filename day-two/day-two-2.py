#!python3

"""
	This is Advent of Code 2021 : Day 2
	Author : Nithesh Balasubramanian
	Date : 13 April 2021
	(Never too late, amirite)
"""

import re

def test():
	return """forward 5
	down 5
	forward 8
	up 3
	down 8
	forward 2
	"""

def load_all():

	instructions = ""
	hor_pos = 0
	depth = 0

	with open("day-two-data/sub-instructions.txt") as f:
		instructions = f.read()

	# comment out line when not testing
	# instructions = test()

	# use regex to extract the command and number
	instructions_list = re.findall(r"(\w*)\s(\d*)\n", instructions)
	aim = 0
	for direction, mvmt in instructions_list:
		if direction=="forward":
			hor_pos += int(mvmt)
			depth += aim*int(mvmt)
		elif direction=="up":
			aim -= int(mvmt)
		elif direction=="down":
			aim += int(mvmt)
		else:
			print("Error, unknown command.")
	
	return hor_pos * depth

print(load_all())