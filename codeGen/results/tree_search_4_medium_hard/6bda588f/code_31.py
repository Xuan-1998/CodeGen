def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[float('inf')] * (2*s + 1) for _ in range(n)]
        dp[0][s] = 0
        for i in range(1, n):
            for j in range(max(0, s - a[i-1]), min(2*s+1, s+a[i-1])):
                if (j-a[i-1]) * (j+a[i-1]-2*s) >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-a[i-1]] + a[i]*a[i])
        print(min(dp[-1]))
