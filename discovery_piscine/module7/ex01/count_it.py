#!/usr/bin/env python3
import sys 
if len(sys.argv) - 1 == 0:
	print("none\n")
else:
	print(f"parameters : {len(sys.argv) - 1}")
	for p in sys.argv[1:]:
		print(f"{p} : {len(p)}")
