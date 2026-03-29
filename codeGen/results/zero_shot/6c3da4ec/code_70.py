import sys

def max_bitwise_or(s):
    n = len(s)
    max_or = 0
    
    # Iterate over all pairs of non-empty substrings
    for i in range(n - 1):
        for j in range(i + 2, n + 1):
            sub1 = int(s[:i], 2) | int(s[i:j], 2)
            sub2 = int(s[j:], 2) | int(s[:j-1], 2)
            
            # Update the maximum OR value if needed
            max_or = max(max_or, sub1, sub2)
    
    return bin(max_or)[2:]

n = int(input())
s = input()
print(max_bitwise_or(s))
