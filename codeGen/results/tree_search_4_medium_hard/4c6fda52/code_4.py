def min_changes(s, k):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(n - k + 2):
            if s[j:j+k] in 'RGBRGBRGB...':
                dp[i][j] = min(dp[i-1][0], dp[i-1][j] if i > j else 0)
            else:
                dp[i][j] = min(dp[i-1][0], dp[i-1][j] if i > j else 0) + (k - 1)
    
    return dp[n][0]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))
    except EOFError:
        break
