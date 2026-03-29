def min_cuts(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True  # Single character is always a palindrome
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:  # Check if characters at start and end match
                dp[i][j] = (length == 2) or dp[i + 1][j - 1]
            else:
                dp[i][j] = False
    
    cuts = 0
    for i in range(n):
        for j in range(i, n):
            if not dp[i][j]:  # If substring is not a palindrome
                cuts += 1
                break
    
    return cuts

s = input()  # Receive input string from stdin
print(min_cuts(s))  # Print the minimum number of cuts to stdout
