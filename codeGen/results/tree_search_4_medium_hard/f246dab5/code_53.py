def calculate_fare(n):
    dp = [[float('inf')] * (n+1) for _ in range(2)]
    
    dp[0][0] = 20
    dp[1][0] = 50
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j < i:
                dp[i][j] = min(dp[i-1][k] + 20 for k in range(j+1))
            elif j == i:
                dp[i][j] = min(50 + dp[max(i-90,0)][0], 120 + dp[max(i-1440,0)][0])
    
    return min(dp[n])

n = int(input())
print(calculate_fare(n))
