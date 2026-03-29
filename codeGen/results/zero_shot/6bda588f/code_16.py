import sys

def min_function_value(a, s):
    n = len(a)
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if a[i - 1] > j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - (a[i - 1] - j)] + a[i - 1] * j)
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][s]

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(min_function_value(a, s))
