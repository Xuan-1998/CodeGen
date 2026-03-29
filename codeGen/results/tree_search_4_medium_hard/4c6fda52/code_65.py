def min_changes():
    n, k = map(int, input().split())
    s = input()
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] == (j - 1) % 3:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + 1
    
    print(dp[n][k])

min_changes()
