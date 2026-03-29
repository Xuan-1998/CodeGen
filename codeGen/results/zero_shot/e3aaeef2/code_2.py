import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + 1
    result = pow(dp[n], m, 10**9+7)
    print(result)
