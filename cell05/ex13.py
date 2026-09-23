#append_it.py

import sys

if (len(sys.argv) == 1):
	print("none")
else:
	for s in sys.argv[1::]:
		print(s + "ism" if s[len(s) - 3:] != "ism" else s)
  