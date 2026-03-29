import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    n, *ks, *hs = map(int, sys.stdin.readline().strip().split())
    dp = [[0] * (max(ks) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(max(0, ks[i-1]-1), max(ks) + 1):
            if j >= ks[i - 1]:
                dp[i][j] = min(dp[i-1][max(0, j-ks[i-1])+1] + hs[i-1], j)
            else:
                dp[i][j] = dp[i-1][j]
                
    print(min(dp[n]))
