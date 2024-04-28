def longest_palindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]

    max_len = 0
    start = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if S[i] == S[j]:
                if j - i < 3:  # Single character or two characters are always palindromes
                    dp[i][j] = True
                elif not dp[i + 1][j - 1]:  # Check the substring in between
                    dp[i][j] = True

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i

    return S[start:start + max_len]
