# Read input from standard input
n = int(input())
s = input()

# Initialize maximum bitwise OR value
max_or = 0

# Iterate over all possible pairs of non-empty substrings
for i in range(n):
    for j in range(i + 1, n):
        # Calculate bitwise OR of current pair of substrings
        or_value = int(s[i:j+1], 2) | int(s[j+1:], 2)
        
        # Update maximum bitwise OR value if needed
        max_or = max(max_or, or_value)

# Print the maximum possible bitwise OR value in binary representation without leading zeroes
print(bin(max_or)[2:])
