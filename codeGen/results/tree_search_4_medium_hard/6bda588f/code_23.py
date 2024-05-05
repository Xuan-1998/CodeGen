import sys
input = lambda: [int(x) for x in input().split()]

t = int(input())
dp = [[sys.maxsize] * (2e5 + 1) for _ in range(2e5 + 1)]
for _ in range(t):
    n, s = input()
    a = input()
    
    dp[0][s] = 0
    for i in range(n):
        for j in range(2e5 + 1):
            if (j - s) * (a[i] - j) >= 0:
                dp[i+1][j+a[i]] = min(dp[i+1][j+a[i]], a[i] * (a[i] - j) + dp[i][j])
    
    print(min(dp[n]))
