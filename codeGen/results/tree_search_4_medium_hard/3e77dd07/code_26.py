def is_scrambled(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False

    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                continue
            if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif i > 0 or j > 0:
                for k in range(1, n):
                    if (s1[i - 1] == s2[k] and
                            dp[0][k - 1] and dp[i - 1][n - 1]):
                        dp[i][j] = True
            else:
                return False

    return dp[n][n]

# Example usage:
s1 = "rkqle"
s2 = "qlker"
print(is_scrambled(s1, s2))  # Output: True
