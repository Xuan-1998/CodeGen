def partition_palindromic(s):
    n = len(s)
    max_length = 1 << (n.bit_length() - 1)  # calculate the maximum allowed palindrome size
    dp = [[[] for _ in range(max_length + 1)] for _ in range(n + 1)]

    def is_palindrome(substring):
        return substring == substring[::-1]

    for i in range(n + 1):
        for j in range(1, min(i + 1, max_length + 1)):
            if i < j:
                dp[i][j] = []
            elif i >= j and is_palindrome(s[i - j:i]):
                dp[i][j] = [s[i - j:i]] + (dp[i - j][j - 1] or [])
            else:
                dp[i][j] = [(dp[i - 1][j - 1] or []) if i > 0 and is_palindrome(s[:i]) else []] + (dp[i - 1][j] or [])

    return dp[n][max_length]

s = input()
print(partition_palindromic(s))
