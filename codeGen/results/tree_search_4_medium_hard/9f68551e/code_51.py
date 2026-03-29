import sys

def min_mana(n, k, h):
    dp = [[0] * (n + 1) for _ in range(2)]
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                dp[1][j] = max(h[i-1], dp[0][i-1])
            else:
                dp[1][j] = min(dp[0][max(0, i-k[i-1]-1)] + k[i-1] for _ in range(k[i-1]+1))
    
    return dp[1][-1]

n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

print(min_mana(n, k, h))
