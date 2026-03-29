def min_portal_moves(n, p):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[p[i - 1] - 1], dp[i - 1]) + 1

    return dp[n]. % (10**9 + 7)

n = int(input())
p = list(map(int, input().split()))
print(min_portal_moves(n, p))
