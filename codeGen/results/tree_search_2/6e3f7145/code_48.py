def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Initialize base case
    for i in range(n):
        dp[i][i] = 1

    max_length = 0
    max_palindrome = ""

    # Fill up the table using bottom-up approach
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    max_palindrome = s[i:j+1]

    return max_palindrome


# Example usage
s = input()
print(longest_palindrome(s))
