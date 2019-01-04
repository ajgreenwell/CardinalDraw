"""
This module contains a dictionary that maps regular expression strings to the number of arguments required for them.
Each regex string is referenced, compiled, and used to find syntax errors in CardinalDraw.py

Written by: Andrew Greenwell
Last edited: Jan 3, 2019
"""

num_args = {
	'^([DU]) *$': 0,
	'^([NSEW]) ([0-9]*) *$': 1
}