def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    cuts = 0
    is_palindrome = False
    for i in range(n - 1, -1, -1):
        if not dp[0][i]:
            if is_palindrome:
                cuts += 1
            is_palindrome = False
        else:
            is_palindrome = True
    
    return cuts

s = input()
print(min_cuts(s))
