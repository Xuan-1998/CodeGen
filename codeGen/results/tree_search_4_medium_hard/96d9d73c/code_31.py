import sys
from collections import defaultdict

def is_possible_partition(n, k, m):
    dp = defaultdict(bool)
    dp[(1, 1)] = True
    for i in range(2, n+1):
        for j in range(1, min(i, k)+1):
            if not dp[(i-1, j-1)]:
                continue
            max_val = -1
            partitions = 0
            for x in A[i-k:i]:
                if x > max_val + m:
                    partitions += 1
                    max_val = x
                else:
                    max_val = max(max_val, x)
            if partitions <= j-1:
                dp[(i, j)] = True
    return dp[(n, k)]

# Input handling
n, k, m = map(int, input().split())
A = list(map(int, input().split()))

print(is_possible_partition(n, k, m))
