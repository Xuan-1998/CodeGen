def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n+1):
        total_players = sum(s[:i])
        if h <= i:
            numerator = sum(dp[j] for j in range(h, i+1))
            denominator = i - h + 1
            dp[i] = (numerator / denominator) * (m - h) / m
        else:
            dp[i] = 0
    
    return 1 - dp[n]

print(solve())
