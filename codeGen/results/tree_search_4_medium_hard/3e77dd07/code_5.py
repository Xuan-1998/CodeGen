def is_scrambled(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[False] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j == 0:
                continue
            elif i == 0 or j == 0:
                dp[i][j] = s1[:i] == s2[:j]
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] and is_scrambled(s1[:i-1], s2[:j-1])
                else:
                    dp[i][j] = any(dp[i-k][j-k] for k in range(min(i, j)+1) if is_scrambled(s1[:i-k], s2[:j-k]))

    return dp[n][m]

# Example usage:
s1 = input()
s2 = input()
print(is_scrambled(s1, s2))
