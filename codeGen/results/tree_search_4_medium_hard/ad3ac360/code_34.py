def min_cuts(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True  # Single character is always palindromic
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:  # If the characters at both ends are equal
                dp[i][j] = (length == 2 or dp[i+1][j-1])  # Check if the substring is palindromic
            else:
                dp[i][j] = False
    
    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1
    
    return cuts
