import sys

# Read input
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Check if k is greater than or equal to n
if k >= n:
    # Duplicate the string until it reaches the desired length
    s = s * (k // n) + s[:k % n]
