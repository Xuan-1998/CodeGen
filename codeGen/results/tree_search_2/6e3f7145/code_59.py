def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (length == 2) or dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    max_length = 0
    longest_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    longest_palindrome = s[i:j+1]

    return longest_palindrome

# Example usage:
s = input()
print(longest_palindrome(s))
