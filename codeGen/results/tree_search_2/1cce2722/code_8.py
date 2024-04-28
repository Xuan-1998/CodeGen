def max_points(ainput):
    n = int(input())
    seq = list(map(int, input().split()))
    
    dp = {i: 0 for i in range(n+1)}
    if n > 0:
        dp[0] = 0
        for s in range(1, n+1):
            i = seq[s-1]
            dp[s] = max(dp.get(s-1, 0) + (s+1), 
                        sum(dp[i-1] for i in range(max(0, s-1), min(s+1, n))))
    
    return dp[n]

print(max_points(input()))
