def isScramble(s1, s2):
    n = len(s1)
    m = len(s2)

    def dfs(i, j):
        if i == 0:
            return s2[:j] == s1
        if j == 0:
            return s2[i:] == s1

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        for k in range(1, n):
            if s1[k - 1] == s1[0]:
                if dfs(k, j):
                    dp[0][j] = True
                if dfs(i, m - j):
                    dp[i][0] = True

        for i in range(n):
            for j in range(m):
                if (s1[i] == s2[j]):
                    if i + 1 > n // 2 or j + 1 > m // 2:
                        return False
                    for k in range(1, n - i):
                        if not dfs(i, k) or not dfs(n - i - 1, m - j - k):
                            return False

        return dp[n - 1][m - 1]

    return dfs(n, m)

s1 = input().strip()
s2 = input().strip()

if isScramble(s1, s2):
    print("Yes")
else:
    print("No")
