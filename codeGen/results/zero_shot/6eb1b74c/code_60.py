import sys
from collections import defaultdict

# Read input
t = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
s = [sys.stdin.readline().strip() for _ in range(n)]

# Preprocess strings
string_indices = {}
for i, s_i in enumerate(s):
    string_indices[s_i] = i

# Initialize variables
m = 0
prev_index = -1
used_strings = set()

while True:
    # Find the next substring to use
    for i, c in enumerate(t):
        if c not in used_strings and i > prev_index:
            for s_i in string_indices:
                if s_i.startswith(c[i-prev_index:i]):
                    m += 1
                    print(f"{string_indices[s_i]} {i}")
                    prev_index = i
                    used_strings.add(s_i)
                    break

    # Check if all characters are colored
    if len(used_strings) == len(t):
        break

# If not all characters were colored, print -1
if len(used_strings) < len(t):
    print(-1)
