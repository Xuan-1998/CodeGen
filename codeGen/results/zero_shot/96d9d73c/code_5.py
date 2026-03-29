import sys

# Read input from stdin
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# Sort the array
A.sort()

# Find the minimum and maximum values
min_val = A[0]
max_val = A[-1]

# Check if it's possible to partition the array
if max_val - min_val > M:
    print(False)
else:
    print(True)
