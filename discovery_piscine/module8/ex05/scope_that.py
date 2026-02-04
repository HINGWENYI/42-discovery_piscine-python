#!/usr/bin/env python3
import sys
def add_one(var):
	if isinstance(var, int):
		return print(int(var + 1))
	elif isinstance(var, float):
		return print(float(var + 1.0))
	else:
		return print(var + "1")	
add_one(10)
add_one(2.1)
add_one("11")

