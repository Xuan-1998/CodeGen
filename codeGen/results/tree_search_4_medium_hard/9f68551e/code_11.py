def min_mana_time(n, k, h):
    dp = [[0 for _ in range(max(k))] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(max(k)+1):
            if j < k[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                min_mana = float('inf')
                for x in range(1, min(j, h[i-1]) + 1):
                    min_mana = min(min_mana, dp[i-1][j-x] + x)
                dp[i][j] = min_mana
    
    return dp[n][max(k)]

while True:
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    
    if not (n and k and h):
        break
    
    print(min_mana_time(n, k, h))
