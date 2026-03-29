# Read input
n = int(input())
s = input()

# Initialize maximum possible value
max_value = 0

# Iterate over all pairs of non-empty substrings in s
for i in range(n):
    for j in range(i + 1, n):
        # Calculate bitwise OR of integer values of two substrings
        substring1 = int(s[i:j+1], 2)
        substring2 = int(s[j:], 2) if j == n - 1 else int(s[j+1:], 2)
        or_value = substring1 | substring2
        
        # Update maximum possible value
        max_value = max(max_value, or_value)

# Print the maximum possible value in binary representation without leading zeroes
print(bin(max_value)[2:].zfill(len(bin(n)) - 2).upper())
