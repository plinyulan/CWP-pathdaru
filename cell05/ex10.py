#parameter_matching.py

import sys

while (len(sys.argv) == 2):
	s = input("What was the parameter? ")
	if (s == sys.argv[1]):
		print("Good Job!")
	else:
		print("Nope, sorry...")
	exit()
print("none")