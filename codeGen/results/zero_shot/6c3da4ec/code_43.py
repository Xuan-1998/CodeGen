# Read the input from stdin
n = int(input())
s = input()

# Initialize the maximum possible value
max_value = 0

# Iterate over all possible pairs of substrings in s
for i in range(n):
    for j in range(i+1, n):
        # Calculate the bitwise OR of the integer values of the two substrings
        a = int(s[:i], 2)
        b = int(s[i:j], 2)
        or_value = a | b
        
        # Update the maximum possible value if necessary
        max_value = max(max_value, or_value)

# Print the answer to stdout
print(bin(max_value)[2:])
