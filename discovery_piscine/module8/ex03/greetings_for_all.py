#!/usr/bin/env python3
def greetings(name="noble stranger"):
	if isinstance(name, str):
		return print("Hello," + name)
	else:
		return print("Error! It was not a name.")
greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)
