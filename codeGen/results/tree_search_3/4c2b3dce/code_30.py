import sys

# Read the input string from stdin
s = input().strip()

# Initialize our state variables
ab_seen = False
ba_seen = False

# Iterate over the string with a sliding window of size 2
for i in range(len(s) - 1):
    if s[i:i+2] == "AB" and not ab_seen:
        ab_seen = True
    elif s[i:i+2] == "BA" and not ba_seen:
        ba_seen = True

# Check if both 'AB' and 'BA' have been seen
if ab_seen and ba_seen:
    print("YES")
else:
    print("NO")
