import sys

# Read input from stdin
s = input()

last_A = -1  # Last occurrence of 'A'
last_B = -1  # Last occurrence of 'B'

for i in range(len(s)):
    if s[i] == 'A':
        last_A = i
    elif s[i] == 'B':
        last_B = i

# Check for "AB" and "BA"
if (last_A != -1 and last_B != -1) and (last_B - last_A > 0):
    print("YES")
else:
    print("NO")
