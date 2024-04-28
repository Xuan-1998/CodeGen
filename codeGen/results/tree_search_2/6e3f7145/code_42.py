def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    max_len = 0
    center_idx = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if i + 1 == j or dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    if j - i > max_len:
                        max_len = j - i
                        center_idx = (i, j)
    return s[center_idx[0]:center_idx[1]+1]

input_str = input()
print(longest_palindrome(input_str))
