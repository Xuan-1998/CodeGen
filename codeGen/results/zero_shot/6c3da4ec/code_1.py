import sys

def max_bitwise_or(s):
    n = len(s)
    
    # Initialize max_or to store the maximum bitwise OR value
    max_or = 0
    
    # Generate all possible substrings
    for i in range(n):
        for j in range(i+1, n+1):
            substring1 = s[i:j]
            
            # Calculate integer values of both substrings
            val1 = int(substring1, 2)
            val2 = int(s[:i]+s[j:], 2)
            
            # Perform bitwise OR operation for the current substring pair
            or_val = val1 | val2
            
            # Update max_or if the current OR value is larger
            max_or = max(max_or, or_val)
    
    return bin(max_or)[2:]

n = int(input())
s = input()

print(max_bitwise_or(s))
