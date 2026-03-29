import sys
from collections import defaultdict

def solution():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[0.0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, m+1):
        if s[i-1] >= n:
            dp[n][i] = 1.0
            break

    for i in range(n+1):
        dp[i][0] = 1.0

    for j in range(1, m+1):
        for i in range(n, -1, -1):
            if s[j-1] >= i:
                p1 = dp[max(i-s[j-1], 0)][j-1]
                p2 = 1.0 - p1
                dp[i][j] = max(dp[i][j-1], p2)
            else:
                dp[i][j] = dp[i][j-1]

    if h > m or s[h-1] < n:
        print(-1.0)
    else:
        print(max(0.0, 1.0 - dp[n][h]))

solution()
