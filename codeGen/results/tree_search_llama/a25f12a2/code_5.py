def solve():
    heads, tails = map(int, input().split())
    
    dp = [[float('inf')] * (tails + 1) for _ in range(heads + 1)]
    dp[0][0] = 0
    
    for i in range(1, heads + 1):
        for j in range(1, tails + 1):
            if i < j:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 2)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
    
    if all(x != float('inf') for x in dp[-1]):
        return [dp[-1].index(float('inf')) - 1, heads - dp[-1].index(float('inf')) - 1]
    else:
        return "No solutions"
