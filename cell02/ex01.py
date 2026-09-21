inp = input()
if not inp.isdigit():
	print("InputError: only numbers")
	exit()
num = int(inp)

print("This number is positive." if num > 0 else "This number is negative." if num < 0 else "This number is both positive and negative.")