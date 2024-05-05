import sys
from collections import defaultdict

# Read input and preprocess prefix sums
n, q = map(int, input().split())
signs = list(input())

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + (1 if signs[i] == '+' else -1)

# Initialize dp and queries
dp = defaultdict(int)
queries = []

for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

# Perform dynamic programming with tabulation
dp[0][n] = [0]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if prefix_sum[i] - prefix_sum[j] == 0:
            dp[i][j] = 0
        else:
            min_remove = float('inf')
            for k in range(j):
                remove_left = dp[i][k]
                remove_right = dp[k][j]
                sign_sum = prefix_sum[i] - prefix_sum[k]
                if abs(sign_sum) == 1:
                    continue
                min_remove = min(min_remove, remove_left + remove_right)
            dp[i][j] = min_remove

# Print answers
for l, r in queries:
    print(dp[l][r])
