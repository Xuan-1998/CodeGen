import sys
from collections import defaultdict

# Read input from stdin
s = sys.stdin.readline().strip()

# Count frequency of 'A' and 'B'
freq_A, freq_B = 0, 0
for c in s:
    if c == 'A':
        freq_A += 1
    elif c == 'B':
        freq_B += 1

if (freq_A > freq_B) or (freq_A == freq_B):
    # If frequency of 'A' is more than 'B', or vice versa, 
    # then it's not possible to have both "AB" and "BA" substrings.
    print("NO")
else:
    # Check for "AB" or "BA" substring
    has_AB = False
    has_BA = False
    last_seen_A = -1
    last_seen_B = -1

    for i in range(len(s)):
        if s[i] == 'A' and (last_seen_A == -1 or s[last_seen_A + 1:i].count('B') > 0):
            has_AB = True
            last_seen_A = i
        elif s[i] == 'B' and (last_seen_B == -1 or s[last_seen_B + 1:i].count('A') > 0):
            has_BA = True
            last_seen_B = i

    if has_AB and has_BA:
        print("YES")
    else:
        print("NO")

