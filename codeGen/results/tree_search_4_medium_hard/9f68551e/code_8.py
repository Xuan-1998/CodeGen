def min_mana(n, k, h):
    dp = [[float('inf')] * (max(h) + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        if i == 0:
            continue
        
        for j in range(1, max(h) + 1):
            if j < h[0]:
                dp[i][j] = float('inf')
            elif k[i - 1] >= j:
                dp[i][j] = min(dp[i - 1][h[i - 1]] + (k[i - 1] - h[i - 1]), dp[i][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][max(h)]

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(min_mana(n, k, h))
