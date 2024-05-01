from collections import defaultdict

def maxPoints(a):
    n = len(a)
    dp = [[0] * 106 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for k in range(105):
            if a[i - 1] == k:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 1] - 2) if i > 1 and (a[i - 2] == k - 1 or a[i - 2] == k + 1) else dp[i - 1][k]
            elif a[i - 1] == k - 1:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - 2] - 2) if i > 1 and (a[i - 2] == k or a[i - 2] == k + 1) else dp[i - 1][k]
            elif a[i - 1] == k + 1:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k + 2] - 2) if i > 1 and (a[i - 2] == k or a[i - 2] == k - 1) else dp[i - 1][k]
    return dp[n][0]

n = int(input())
a = list(map(int, input().split()))
print(maxPoints(a))
