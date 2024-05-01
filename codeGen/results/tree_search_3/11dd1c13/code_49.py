import sys
from collections import defaultdict

# Get the size of the grid
n = int(input())

# Initialize the memo dictionary to store previously computed values
memo = defaultdict(lambda: [float('inf')] * n)

# Base case: dp[0][j] = 0 for all j
for j in range(n):
    memo[(0, j)] = 0

# Fill up the memo dictionary using dynamic programming
for i in range(1, n):
    for j in range(i+1):
        if j > 0:
            # Calculate the minimum sum considering the current element and the elements below it
            min_sum = sys.maxsize
            for k in range(j+1, n):
                min_sum = min(min_sum, memo[(i-1, k-1)][k-j] + int(input()) if i > 0 else 0)
            memo[(i, j)] = min_sum
        else:
            # The first column is treated separately since we can't move left
            memo[(i, j)] = int(input())

# Find the minimum sum of a falling path with non-zero shifts
min_sum = sys.maxsize
for j in range(n):
    min_sum = min(min_sum, memo[(n-1, j)])

print(min_sum)
