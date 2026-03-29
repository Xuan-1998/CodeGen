def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        dp = [[float('inf')] * (s+1) for _ in range(n+1)]
        dp[0][s] = 0
        for i in range(1, n+1):
            for k in range(s-1, -1, -1):
                if k + a[i-1] <= s:
                    dp[i][k] = min(dp[i][k], (s-k) * (a[i-1]-s) + dp[i-1][k-a[i-1]])
                else:
                    dp[i][k] = dp[i-1][k+a[i-1]]
        print(min(dp[n]))

if __name__ == "__main__":
    solve()
