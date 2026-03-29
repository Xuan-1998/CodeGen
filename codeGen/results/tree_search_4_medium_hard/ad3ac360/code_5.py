def min_cuts(s):
    n = len(s)
    memo = {}

    def is_palindrome(s, i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= j:
            return True  # single character or empty string is always palindromic
        if s[i] == s[j]:
            if j - i < 2:  # single character or two characters are always palindromes
                return True
            if i + 1 >= j:  # no need to check the middle part
                return False
            memo[(i, j)] = (s[i] == s[j]) and is_palindrome(s, i + 1, j - 1)
        else:
            memo[(i, j)] = False
        return memo[(i, j)]

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            dp[i][j] = is_palindrome(s, i, j)

    cuts = 0
    for i in range(1, n):
        if not dp[0][i]:
            cuts += 1

    return cuts + 1
