import sys
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if sum(b[:j]) == b[i - 1]:
                dp[i][j] = any(dp[k][j - 1] for k in range(j))
    
    print("YES" if dp[n][n] else "NO")
