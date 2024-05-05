import sys

def solve(n, k):
    s = sys.stdin.readline().strip()
    
    # If the original string is shorter than k, we need to duplicate it
    if n < k:
        return s * (k // n) + (s[:k % n] if k % n != 0 else '')
    
    # If the last character of the string is the smallest lexicographically,
    # we can delete it and get a smaller string of length k-1.
    # We then repeat this process until we have a string of length k.
    while len(s) > k:
        s = s[:-1]
    
    return s.ljust(k)

n, k = map(int, sys.stdin.readline().split())
print(solve(n, k))
