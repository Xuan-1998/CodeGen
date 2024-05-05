import sys

def solve():
    n = int(input())
    costs = [0] * (n + 1)
    for i in range(1, n + 1):
        costs[i] = int(input())

    dp = [[-1] * 100000 for _ in range(n + 1)]
    dp[0][0] = 0

    max_j = 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[j-1][costs[j-1]] + costs[i])
            else:
                dp[i][j] = costs[i]
            max_j = max(max_j, i)

    return -1 if dp[n][max_j] == -1 else dp[n][max_j]

print(solve())
