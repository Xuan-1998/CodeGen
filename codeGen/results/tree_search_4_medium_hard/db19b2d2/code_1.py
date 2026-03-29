def prob():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = 1 - (s[h-1] / sum(s)) * (1 - dp[i-1])
    
    if dp[n] >= 1e-6:
        print(dp[n])
    else:
        print(-1)
