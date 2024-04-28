s = input().strip()
t = input().strip()

def shortest_uncommon_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    res = m
    for i in range(m):
        if not any(s[i] == c and j < n for c, j in enumerate(t)):
            res = min(res, dp[i][n])
    
    return res if res != m else -1

print(shortest_uncommon_subsequence(s, t))
