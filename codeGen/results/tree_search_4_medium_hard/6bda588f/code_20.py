from collections import defaultdict

def min_f(a, s):
    n = len(a)
    dp = [[float('inf')] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(s + 1):
            if j < a[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i - 1]] + a[i - 1] * (s - j) + j * (s - j))
    
    return dp[n][s]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a, s))
