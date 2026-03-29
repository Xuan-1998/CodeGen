def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[float('inf')] * (s + 1) for _ in range(n)]
        dp[0][0] = 0
        
        for i in range(1, n):
            for k in range(s + 1):
                if a[i - 1] > s:
                    dp[i][k] = min(dp[i - 1][max(0, k - a[i - 1] + s)] + a[i - 1] * (s - max(0, k - a[i - 1] + s)))
                else:
                    dp[i][k] = min(dp[i - 1][max(0, k - a[i - 1])] + a[i - 1] * (k - max(0, k - a[i - 1])))
        
        print(min(dp[-1]))

solve()
