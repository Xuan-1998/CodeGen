def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Fill the table row by row, starting from the top-left corner
    for i in range(n):
        dp[i][i] = 1  # Single characters are always palindromes

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 0

    # Find the maximum palindromic substring
    max_length = 0
    max_palindrome = ""
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    max_palindrome = s[i:j+1]

    return max_palindrome

# Example usage
s = input()
print(longest_palindromic_substring(s))
