#!/usr/bin/env python3
def array_of_names(dict):
	names = []
	for key, value in dict.items():
		name = key.capitalize() + " " + value.capitalize()
		names.append(name)
	return names
persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))
