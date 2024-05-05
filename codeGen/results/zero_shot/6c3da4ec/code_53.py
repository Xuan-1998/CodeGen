import sys

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# Initialize maximum bitwise OR value
max_or = 0

# Iterate over all possible pairs of substrings
for i in range(n):
    for j in range(i + 1, n):
        # Calculate the bitwise OR of the two substrings
        or_val = int(s[i:j+1], 2) | int(s[j:]+s[:i], 2)
        
        # Update the maximum bitwise OR value if necessary
        max_or = max(max_or, or_val)

# Print the maximum bitwise OR value in binary representation without leading zeroes
print(bin(max_or)[2:])
