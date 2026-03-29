n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    stuffings.append((a, b, c, d))

def max_profit(n, m):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        if i > 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[0][i] = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if stuffings[i-1][2] <= j and stuffings[i-1][3] + stuffings[i-1][1]*j > dp[i-1][j]:
                dp[i][j] = stuffings[i-1][3] + stuffings[i-1][1]*j
            else:
                dp[i][j] = dp[i-1][j]
    
    return max(max(dp[i]) for i in range(m+1))

print(max_profit(n, m))
