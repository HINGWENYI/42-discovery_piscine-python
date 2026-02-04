#!/usr/bin/env python3
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2]) + 1
if len(sys.argv) != 3:
	print("none\n")
elif num1 >= num2:
	print("none\n")
else:
	print(list(range(num1, num2)))
