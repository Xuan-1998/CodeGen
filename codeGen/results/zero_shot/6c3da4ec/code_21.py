import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

max_or = 0  # Initialize maximum bitwise OR value to 0

# Generate all possible pairs of substrings
for i in range(n):
    for j in range(i+1, n):
        substring1 = s[i:j+1]
        for k in range(j+1, n):
            substring2 = s[j:k+1]
            
            # Calculate bitwise OR of the two substrings
            or_value = int(substring1, 2) | int(substring2, 2)
            
            # Update maximum bitwise OR value if necessary
            max_or = max(max_or, or_value)

print(bin(max_or)[2:])  # Print the binary representation without leading zeroes
