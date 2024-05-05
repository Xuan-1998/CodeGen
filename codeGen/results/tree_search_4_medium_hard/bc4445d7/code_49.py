import sys
from functools import lru_cache

# Read input and define variables
n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = list(map(int, input().split()))

# Define the recursive function to calculate dp[i]
@lru_cache(None)
def dp(i):
    return sum(f(i, j) * (1 + dp[j]) for j in range(n) if f(i, j) and j != i)

# Calculate the maximum possible distribution index
max_distribution_index = 0
for u, v in edges:
    max_distribution_index += f(u, v)
print(max_distribution_index % (10**9 + 7))

