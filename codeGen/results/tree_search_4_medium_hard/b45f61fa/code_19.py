import sys
from functools import lru_cache

# Read input from standard input
n = int(input())
p = [int(x) for x in input().split()]

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return 0
    cost = float('inf')
    for k in range(i+1, j+1):
        cost = min(cost, dp(i, k-1) + p[i]*p[k]*p[j])
    return cost

# Calculate the minimum cost
min_cost = dp(0, n-2)

# Print the optimal parenthesization
for i in range(n-1):
    if i == 0:
        print('(', end='')
    if i < n-2:
        print('A', end='*')
    if i > 0 and i < n-2:
        print(')*(', end='')
    else:
        print('A', end=')')

print()
