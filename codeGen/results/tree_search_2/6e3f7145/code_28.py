def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Extend to longer substrings
    max_length = 1
    result = s[0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    max_length = max(max_length, j - i + 1)
                    result = s[i:j+1]
    return result

s = input()
print(longest_palindrome(s))
