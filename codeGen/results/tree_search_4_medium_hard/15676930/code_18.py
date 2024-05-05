def max_joy():
    n = int(input())
    a, b, c = [int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            dp[i][0] = c[0]
        else:
            dp[i][0] = max(c[i-1], a[i-1] + dp[i-1][0])
        
        for j in range(1, min(i, j+1) + 1):
            if j == 1:
                dp[i][j] = max(a[i-1] + dp[i-1][j-1], b[i-1] + dp[i-1][j], c[i-1] + dp[i-1][j+1])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    
    return dp[n][0]

print(max_joy())
