import sys

# Read input from stdin
N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# Sort the array
A.sort()

# Initialize variables
max_val = A[-1]
partitions = 0

for i in range(N):
    if A[i] > max_val + M:
        # Start a new partition
        partitions += 1
        max_val = A[i]

if partitions >= (N - K) // K:
    print("true")
else:
    print("false")
