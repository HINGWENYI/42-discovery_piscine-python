#!/usr/bin/env python3
import sys
if len(sys.argv) <= 2:
	print("none\n")
else:
	for arg in sys.argv[1:][::-1]:
		print(arg)
