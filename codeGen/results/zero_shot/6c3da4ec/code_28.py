import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_or = 0
for i in range(n):
    for j in range(i+1, n):
        # Generate the first substring (from index i to j)
        substr1 = s[i:j+1]
        
        # Generate the second substring (from index j+1 to the end)
        substr2 = s[j+1:]
        
        # Calculate the bitwise OR operation between the two substrings
        or_val = int(substr1, 2) | int(substr2, 2)
        
        # Update the maximum possible value if necessary
        max_or = max(max_or, or_val)

print(bin(max_or)[2:])  # Print the maximum possible value in binary representation without leading zeroes.
