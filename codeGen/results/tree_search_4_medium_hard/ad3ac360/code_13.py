def min_cuts(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j]:
                dp[i][j] = (dp[i+1][j-1] or dp[i+1][j-1]) and 1
            else:
                dp[i][j] = 0
    
    cuts = 0
    for i in range(n):
        if dp[i][i + 1]:
            cuts += 1
    
    return cuts

# Test the function
s = input()
print(min_cuts(s))
