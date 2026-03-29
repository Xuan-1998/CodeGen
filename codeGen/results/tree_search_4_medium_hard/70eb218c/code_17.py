import sys

def min_operations(n, x):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if x < 10**(i-1):
            dp[i] = 0
        else:
            for y in range(1, 10):
                if int(str(x*y)[:-1]) >= 10**(i-1):
                    dp[i] = min(dp[i], 1 + dp[i-1])
                    break

    return -1 if dp[n] == float('inf') else dp[n]

n, x = map(int, input().split())
print(min_operations(n, x))
