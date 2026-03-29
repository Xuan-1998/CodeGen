def minCostToSortStrings():
    n = int(input())
    costs = [int(input()) for _ in range(n)]
    strings = [input() for _ in range(n)]

    dp = [[-1] * (max(len(s) for s in strings) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, len(strings[i - 1])), 0, -1):
            dp[i][j] = min(dp[i-1][k] + costs[i-1] if strings[i-1][:k] == strings[i-2][:k] else dp[i-1][j], k > 0 and dp[i-1][j-1])

    return -1 if any(dp[n][i] == -1 for i in range(1, len(strings[0]) + 1)) else sum(costs[:n-1]) + costs[-1] if dp[n][len(strings[-1])] != -1 else -1
