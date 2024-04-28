import sys
from collections import Counter

# Read input from stdin
s = input().strip()

# Count the frequency of 'A' and 'B'
freq_A = s.count('A')
freq_B = s.count('B')

# Determine which character appears more frequently
max_freq = max(freq_A, freq_B)

# Use this information to decide whether the string contains both substrings
if (s.startswith('AB') or s.startswith('BA')) and (max_freq - 1) <= len(s) - 2:
    print("YES")
else:
    print("NO")
