#!/usr/bin/env python3
i = 0
while i <= 10:
	result = f"Table of {i}:"
	j = 0
	while j <= 10:
		result += f" {i * j}"
		j += 1
	print(result)
	i += 1 
