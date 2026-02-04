#!/usr/bin/env python3
import sys
import re
if len(sys.argv) != 2:
	print("none\n")
elif not re.findall(re.escape("z"), sys.argv[1]):
	print("none\n")
else:
	count = len(re.findall(re.escape("z"), sys.argv[1]))
	print("z" * count)

