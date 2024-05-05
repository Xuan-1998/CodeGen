import sys

def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    cuts = 0

    # Initialize the diagonal as True (single-character palindromes)
    for i in range(n):
        dp[i][i] = True

    # Fill up the dynamic programming table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
            cuts += int(not dp[i][j])

    return cuts

s = input()
print(min_cuts(s))
