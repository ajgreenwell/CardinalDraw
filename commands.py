"""
This module contains all function definitions and their corresponding handlers for all available commands.
Any functions prepended by an underscore are considered private and are not to be accessed by clients.

Written by: Andrew Greenwell
Last edited: Jan 3, 2019
"""

import turtle

def _move(dir, dis):
	turtle.seth(dir)
	turtle.forward(dis)

def down():
	turtle.pendown()

def up():
	turtle.penup()

def north(dis):
	_move(90, dis)

def south(dis):
	_move(270, dis)

def east(dis):
	_move(0, dis)

def west(dis):
	_move(180, dis)


handlers = {

	'D': {
		'ARG': None, 
		'func': down
		},

	'U': {
		'ARG': None,
		'func': up
	},

	'N': {
		'ARG': range(0, 1001),
		'func': north
		},

	'S': {
		'ARG': range(0, 1001),
		'func': south
		},

	'E': {
		'ARG': range(0, 1001),
		'func': east
		},

	'W': {
		'ARG': range(0, 1001),
		'func': west
		}

}
