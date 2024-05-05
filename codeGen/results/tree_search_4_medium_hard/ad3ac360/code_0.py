def minCuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
    
    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1
    
    return cuts

if __name__ == "__main__":
    s = input()
    print(minCuts(s))
