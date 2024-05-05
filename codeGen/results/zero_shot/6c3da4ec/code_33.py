import sys

# Read the input
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

# Initialize maximum possible value
max_value = 0

# Iterate over all pairs of substrings
for i in range(n):
    for j in range(i + 1, n):
        # Calculate the bitwise OR of current pair of substrings
        or_value = int(s[i:j+1], 2) | int((s[:i] + s[j:]), 2)
        
        # Update maximum possible value if necessary
        max_value = max(max_value, or_value)

# Print the maximum possible value
print(bin(max_value)[2:].zfill(n).lstrip('0') or '0')
