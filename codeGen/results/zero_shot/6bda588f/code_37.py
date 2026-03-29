def min_f(a, s):
    n = len(a)
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(s + 1):
            if a[i - 1] > j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][a[i - 1] - j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][s]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a, s))
