import sys
from collections import defaultdict

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

# Initialize dp array
dp = [[0] * (max(k) + 1) for _ in range(n + 1)]

# Calculate minimum mana required for each monster's health at every possible second
for i in range(1, n + 1):
    for j in range(k[i - 1], k[i]):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][k[i - 2]] + (j - k[i - 2]))

# Calculate minimum mana required to kill all monsters
min_mana = float('inf')
for i in range(n, -1, -1):
    if h[i] <= k[i]:
        min_mana = min(min_mana, dp[i][k[i]])
        break

print(min_mana)
