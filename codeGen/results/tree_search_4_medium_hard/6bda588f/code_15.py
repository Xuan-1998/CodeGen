def read_input():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[float('inf')] * (s + 2) for _ in range(n - 1)]
        dp[0][s] = 0
        
        for i in range(1, n - 1):
            for k in range(s + 1):
                if a[i] <= k:
                    dp[i][k] = min(dp[i][k], dp[i - 1][k - a[i]] + a[i])
        
        print(min(dp[-1]))

read_input()
