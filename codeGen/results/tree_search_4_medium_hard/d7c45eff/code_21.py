def smallest_string(n, k):
    s = input().strip()
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        if i == n or k == 0:
            dp[i][k] = s[:i]
        else:
            if s[i-1] < s[i]:
                dp[i][k] = min(dp[i-1][k], dp[i-1][k-1] + s[i-1])
            elif i > 0 and k > 0:
                dp[i][k] = min(dp[i-1][k], dp[i][k-1] + s[i-1])
    
    return dp[n][k]

n, k = map(int, input().split())
print(smallest_string(n, k))
