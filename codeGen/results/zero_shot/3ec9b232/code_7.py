# Read input
n = int(input())
m = list(map(int, input().split()))

# Initialize count of valid collections
count = 0

# Iterate over all possible subsets of M
for i in range(1 << n):
    subset = [m[j] for j in range(n) if (i >> j) & 1]
    
    # Check if merging the subset into a sorted array gives M
    if merge(subset) == m:
        count += 1

# Print the result modulo 10^9+7
print(count % (10**9 + 7))


def merge(arr):
    return sorted(arr)
