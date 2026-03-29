def is_scrambled(s1, s2):
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = (i > 1 and j > 1) and dp[i-1][j-1]
            else:
                dp[i][j] = any(dp[k][l] for k in range(i) for l in range(j))

    return dp[-1][-1]

# Test cases
s1, s2 = input().split()
print(is_scrambled(s1, s2))
