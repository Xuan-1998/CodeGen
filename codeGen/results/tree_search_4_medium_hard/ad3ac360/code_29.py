def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n + 1):
            if s[i:j].lower() == s[i:j][::-1].lower():
                dp[i][j] = True
            else:
                min_cuts = float('inf')
                for k in range(i, j):
                    if dp[i][k] and dp[k + 1][j]:
                        min_cuts = min(min_cuts, 1 + (dp[i][k] or dp[k + 1][j]))
                dp[i][j] = min_cuts
    
    return dp[0][n - 1]

s = input()
print(min_cuts(s))
