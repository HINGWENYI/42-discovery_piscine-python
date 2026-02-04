#!/usr/bin/env python3
import sys
if len(sys.argv) - 1 == 0:
	print("none\n")
else:
	for word in sys.argv[1:]:
		if word.find("ism", len(word) - 3) != -1:
			continue
		else:
			print(word + "ism")

