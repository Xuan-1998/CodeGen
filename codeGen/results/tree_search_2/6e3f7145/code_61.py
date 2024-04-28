def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1  # single characters are palindromes

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = 0

    max_length = 0
    max_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            if dp[i][j] == 1 and j - i + 1 > max_length:
                max_length = j - i + 1
                max_palindrome = s[i:j+1]

    return max_palindrome

# Example usage:
s = input()
print(longest_palindrome(s))
