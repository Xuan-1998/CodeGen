def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    max_length = 1
    start = 0

    for i in range(n):
        for j in range(i + 1):
            if s[j] == s[i]:
                if j + 1 <= i:
                    dp[j][i] = dp[j + 1][i - 1]
                else:
                    dp[j][i] = 1
                if j > start and dp[j][i]:
                    max_length = max(max_length, i - j + 1)
                    start = j

    return s[start:start + max_length]

# Example usage:
s = input()
print(longest_palindrome(s))
