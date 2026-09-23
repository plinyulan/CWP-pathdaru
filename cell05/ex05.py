#aff_first_param.py

import sys

try:
	print(sys.argv[1])
except IndexError:
	print("none")
