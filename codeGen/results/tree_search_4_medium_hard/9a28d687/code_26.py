import sys

# Read input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Initialize DP table
dp = [[0] * (len(strings[0]) + 1) for _ in range(n + 1)]
lens = [len(s) for s in strings]

# Fill DP table
for i in range(1, n + 1):
    for j in range(len(strings[i - 1])):
        revs_needed = len(strings[i - 1]) // 2 + (len(strings[i - 1]) % 2)
        dp[i][j] = min((dp[i - 1][k - 1] if k > 0 else costs[i - 1]) for k in range(revs_needed + 1))
    dp[i][-1] = dp[i-1][-1]

# Calculate the minimum total cost
min_cost = sum(costs) - min(dp[-1])

print(min_cost)
