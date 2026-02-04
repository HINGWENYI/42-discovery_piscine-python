#!/usr/bin/env python3
import sys
def shrink(word):
	return print(word[:8])
def enlarge(word):
	while len(word) < 8:
		word += "Z"
	return print(word)
if len(sys.argv) - 1 == 0:
	print("none\n")
else:
	for str in sys.argv[1:]:
		if len(str) > 8:
			shrink(str)
		elif len(str) < 8:
			enlarge(str)
		else:
			print(str)
