import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][j] = n + 1 if j == 0 else 0
    
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j == 0:
                dp[i][j] = dp[i-1][0]
            elif 2*j <= n:
                dp[i][j] = dp[i-1][0] + sum(dp[i-1][k]) for k in range(n/2+1) else 0
            else:
                dp[i][j] = 1 if i == m else 0
    
    print(sum(dp[m-1][k]) for k in range(n)) % (10**8 + 7)
