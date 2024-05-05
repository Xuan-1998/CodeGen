import sys

def solve(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i + 1):
            if i == j:
                continue
            dp[i][j] = min(dp[i - 1][k] + 1 for k in range(j - 1) if strings[k] != strings[j])

    total_cost = 0
    for i in range(n - 1):
        total_cost += dp[i + 1][i]

    return -1 if total_cost > costs[-1] else total_cost

n = int(input())
strings = [input() for _ in range(n)]
costs = [int(input()) for _ in range(n)]

print(solve(n))
