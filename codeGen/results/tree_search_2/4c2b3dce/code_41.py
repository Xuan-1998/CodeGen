import sys

# Read the input string from stdin
s = sys.stdin.readline().strip()

dp = {'A': 0, 'B': 0}
for c in s:
    if c == 'A':
        dp['A'] += 1
    elif c == 'B':
        dp['B'] += 1

# Check if both counts are greater than 0
if max(dp.values()) > 0 and min(dp.values()) > 0:
    print("YES")
else:
    print("NO")
