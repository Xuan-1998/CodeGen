n = int(input())
for _ in range(n):
    n, *a = map(int, input().split())
    dp = [[False] * 2 for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        if a[i-1] > 0:
            dp[i][0] |= dp[i-1][0]
            dp[i][1] |= dp[i-1][1] or dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0] and (a[i-1] <= 0 or dp[i-1][1])
            dp[i][1] = dp[i-1][1] or dp[i-1][0]
    print("YES" if dp[n][0] else "NO")
