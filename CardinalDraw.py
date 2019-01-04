"""
This is an interpreter for CardinalDraw, a mini-language I've invented
that enables the drawing of lines and shapes using simple, one character commands.

Written by: Andrew Greenwell
Last edited: Jan 3, 2019
"""

import commands as com
import re
import syntax
import sys
import turtle

# returns a tuple containing the match object and the number of arguments if the syntax is valid
# returns None for both if the syntax is invalid
def findMatch(line):
	for exp in syntax.num_args:
		match = re.compile(exp).match(line)
		if match:
			return (match, syntax.num_args[exp])
	return (None, None)


# calls findMatch(line) to determine if the syntax is valid
# if it's not, returns False
# if it is valid, calls the corresponding functions with the proper argument(s) from commands.handlers
def parse(line):
	match, num_args = findMatch(line)
	if not match:
		return False
	if num_args == 0:
		com.handlers[match.group(1)]['func']()
	elif num_args == 1:
		command = match.group(1)
		arg = int(match.group(2))
		if arg not in com.handlers[command]['ARG']:
			return False
		com.handlers[command]['func'](arg)
		


def main():
	turtle.speed(1)
	try:
		filename = sys.argv[1]
		file = open(filename, 'r')
	except:
		print('***InvalidFilenameError*** : File Does Not Exist')
		return
	line_num = 1
	for line in file:
		line = line.rstrip('\n')
		if parse(line) == False:
			print('***SyntaxError*** : {} on Line {}'.format(filename, line_num))
			break
		line_num += 1
	file.close()


if __name__ == '__main__':
	main()

