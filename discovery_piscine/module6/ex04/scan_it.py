#!/usr/bin/env python3
import sys
import re
if len(sys.argv) != 3 or not re.findall(re.escape(sys.argv[1]), sys.argv[2]):
	print("none\n")
else:
	print(len(re.findall(re.escape(sys.argv[1]), sys.argv[2])))
