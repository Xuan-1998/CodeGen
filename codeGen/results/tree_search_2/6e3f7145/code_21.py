def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    max_length = 0
    max_substring = ""

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if i + 1 > j - 1 or dp[i + 1][j - 1]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        max_substring = s[i:j+1]

    return max_substring

# Test the function
s = input()
print(longest_palindromic_substring(s))
