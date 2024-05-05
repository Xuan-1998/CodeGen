def is_scrambled(s1, s2):
    m = len(s1)
    dp = [[False] * (m + 1) for _ in range(m + 1)]

    def dfs(i, j):
        if dp[i][j]:
            return True

        if i == 0 and j == 0:
            return s1 == s2[:m]

        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            dp[i][j] = dfs(i - 1, j - 1)
        elif i > 0 and s1[i - 1] in s2[:j]:
            for k in range(j):
                if s2[k] == s1[i - 1]:
                    dp[i][j] = dfs(i - 1, k) and dfs(i, j - 1)
                    break
        else:
            for k in range(m):
                if s1[k] in s2[:j]:
                    dp[i][j] = dfs(k, j) and dfs(i - 1, j)
                    break

        return dp[i][j]

    return dfs(m, m)

s1 = input().strip()
s2 = input().strip()

print(is_scrambled(s1, s2))
