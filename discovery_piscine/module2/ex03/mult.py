number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
mult = number1 * number2
print(f"{number1} x {number2} = {mult}")
if mult > 0:
	print("The result is positive")
elif mult < 0:
	print("The result is negative")
else:
	print("The result is both positive and negative")
