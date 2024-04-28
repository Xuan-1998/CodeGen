def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    max_len = 0
    result = ""

    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    result = s[i:j+1]

    return result

s = input()
print(longest_palindrome(s))
