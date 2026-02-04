#!/usr/bin/env python3
number = int(input("Enter a number less than 25 : "))
if number <= 25:
	while number <=25:
		print(f"Inside the loop, my variable is {number}")
		number += 1
		if number == 26:
			break
else:
	print("Error") 
