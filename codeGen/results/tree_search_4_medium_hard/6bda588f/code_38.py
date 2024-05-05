t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[float('inf')] * (2*s+1) for _ in range(n)]
    dp[0][s] = 0
    for i in range(1, n):
        for j in range(2*s+1):
            if j - s >= 0 and a[i] - 2*s >= 0:
                dp[i][j] = min(dp[i-1][j+1], dp[i-1][j-1]) + (a[i] - 2*s) * s
    print(min(dp[-1]))
