def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    max_length = 0
    max_palindrome = ""

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    max_palindrome = s[i:j+1]

    return max_palindrome

s = input()
print(longest_palindromic_substring(s))
