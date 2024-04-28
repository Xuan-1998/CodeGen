def longest_palindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    max_len = 0
    res = ""

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    res = s[i:j + 1]

    return res

s = input()
print(longest_palindrome(s))
