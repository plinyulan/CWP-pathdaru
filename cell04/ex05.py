#up_low.py

print("".join([s.lower() if s.upper() == s else s.upper() for s in str(input())]))