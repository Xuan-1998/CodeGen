def min_function_value(n, s, a):
    dp = [[0] * (n + 1) for _ in range(2)]
    
    for i in range(1, n + 1):
        for j in range(2):
            if j == 0:
                dp[j][i] = min(dp[0][i - 1] + a[i - 1] * s, dp[1][i - 1])
            else:
                dp[j][i] = min(dp[j][i - 1], dp[0][i - 1] + a[i - 1] * s)
    
    return dp[1][n]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_function_value(n, s, a))
