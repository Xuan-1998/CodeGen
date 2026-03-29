import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0, False] for _ in range(n + 1)]
    
    for i in range(m):
        ai, bi, ci, di = map(int, input().split())
        
        for j in range(n, -1, -1):
            if j < c0:
                continue
            dp[j][0] = max(dp[j][0], dp[j - c0][0] + di)
            dp[j][1] or= (dp[j - bi][1] and ci <= j)
    
    return dp[n][0]

print(solve())
