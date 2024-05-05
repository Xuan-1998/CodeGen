def isScrambled(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i == 0 and j == 0:
            return True
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            return dfs(i - 1, j - 1)
        if dp[i][j]:
            return True

        for k in range(1, n + 1):
            if (i - k >= 0 and j - k >= 0 and dfs(i - k, j - k) and
                    sorted(s1[i - k:i]) == sorted(s2[j - k:j])):
                dp[i][j] = True
                return True

        return False

    return dfs(n, m)

# Receive input from stdin
s1, s2 = input().split()

# Print the answer to stdout
print(isScrambled(s1, s2))
