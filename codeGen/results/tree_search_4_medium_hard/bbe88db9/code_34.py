def solve():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [float('inf')] * (n+2)
    dp[1] = 0

    for i in range(1, n+1):
        dp[i+1] = min(dp[p[i]] + (i - p[i]) % 2, dp[i-1] + 1)

    return dp[n+1]

print(solve())
