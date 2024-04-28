def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Initialize diagonal cells (single characters are palindromes)
    for i in range(n):
        dp[i][i] = True

    max_length = 0
    result = ""

    # Fill in the rest of the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and length > max_length:
                    max_length = length
                    result = s[i..j]

    return result

s = input()
print(longest_palindrome(s))
