python
# Step 1: Read input
n = int(input())
s = input()

# Step 2: Initialize maximum possible value
max_or = 0

# Step 3: Generate all possible pairs of non-empty substrings
for i in range(n):
    for j in range(i+1, n):
        # Step 4: Calculate bitwise OR of integer values of the pair of substrings
        left = int(s[:i], 2)
        right = int(s[i:j], 2)
        or_val = left | right
        
        # Step 5: Update maximum possible value if necessary
        max_or = max(max_or, or_val)

# Step 6: Convert maximum possible value to binary and remove leading zeroes
max_bin = bin(max_or)[2:]

print(max_bin)
