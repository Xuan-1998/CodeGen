def min_f_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[float('inf')] * (s + 1) for _ in range(n)]
        dp[0][0] = 0
        
        for i in range(1, n):
            for k in range(max(0, s - a[i]), min(s, s + a[i])):
                for x in range(min(k, a[i]), max(k, a[i]) + 1):
                    y = a[i] - x
                    if (x - s) * (y - s) >= 0:
                        dp[i][k] = min(dp[i][k], dp[i-1][k-(a[i]-x)] + x*y)
        
        print(min(dp[n-1]))
