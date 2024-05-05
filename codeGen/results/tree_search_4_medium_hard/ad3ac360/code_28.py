def minCut(s):
    n = len(s)
    table = [[False] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or table[i+1][j-1]):
                table[i][j] = True
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for j in range(i, n):
            if not table[i][j]:
                for k in range(i, j+1):
                    dp[j+1] = min(dp[j+1], 1 + dp[k-1] if k > 0 else 1)
    return max(0, dp[-1])

s = input()
print(minCut(s))
