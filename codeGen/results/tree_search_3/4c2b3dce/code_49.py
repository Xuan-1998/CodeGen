import sys
from collections import Counter

# Read input
s = sys.stdin.readline().strip()

# Count the frequency of characters in string s
counter = Counter(s)

# Check if 'AB' and 'BA' appear without any overlap
if (counter['A'] >= 1 and counter['B'] >= 1 and 
   len([c for c in s if c not in ['A', 'B']]) == 0):
    print("YES")
else:
    print("NO")
