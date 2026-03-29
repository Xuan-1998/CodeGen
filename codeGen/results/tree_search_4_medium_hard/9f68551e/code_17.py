from collections import defaultdict

def min_mana(n, k, h):
    dp = [[float('inf')] * (max(k) + 1) for _ in range(n + 1)]
    
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(max(k[i-1]), -1, -1):
            if j < k[i-1]:
                dp[i][j] = min(dp[i-1][max(0, j)] + 1, float('inf'))
            else:
                dp[i][j] = min(dp[i-1][k[i-1]-1] + (h[i-1]-1), float('inf'))
    
    return min(dp[n])

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(min_mana(n, k, h))
