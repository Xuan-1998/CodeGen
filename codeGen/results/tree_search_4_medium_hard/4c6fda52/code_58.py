def min_changes():
    n, k = map(int, input().split())
    s = input()
    
    # Precompute the minimum number of changes needed for each substring of length k
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    expected_color = 'RGB'[int((n + 2) / 3 % 3)]
    
    for i in range(1, n + 1):
        if s[i - 1] != expected_color:
            dp[i][k] = dp[i - 1][k] + 1
        else:
            dp[i][k] = dp[i - 1][k]
        
        for j in range(min(i, k), 0, -1):
            if s[i - 1] != expected_color:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    
    print(sum([min(dp[i][k], dp[i][k - 1]) for i in range(1, n + 1)]))

if __name__ == "__main__":
    min_changes()
