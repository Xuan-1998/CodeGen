def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 1 if (length == 2 or dp[i+1][j-1]) else 0

    max_length = 0
    max_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    max_palindrome = s[i:j+1]

    return max_palindrome

# Test the function
s = input()
print(longest_palindrome(s))
