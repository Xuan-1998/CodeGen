import sys

def max_bitwise_or(s):
    n = len(s)
    max_value = 0
    
    # Iterate over all possible lengths of the first substring
    for i in range(1, n+1):
        for j in range(i):
            # Calculate the bitwise OR value for the current substrings
            or_value = int(s[j:i], 2) | int(s[i:], 2)
            max_value = max(max_value, or_value)
    
    return bin(max_value)[2:]  # Convert to binary and remove '0b' prefix

n = int(input())
s = input()
print(max_bitwise_or(s))
