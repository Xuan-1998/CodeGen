===BEGIN CODE===
def mergeable(n, p):
    dp = [[0] * (n + 1) for _ in range(2 * n + 1)]

    # Base case: empty arrays
    for j in range(n + 1):
        dp[0][j] = 1

    for i in range(1, 2 * n):
        for j in range(1, min(i + 1, n) + 1):
            if p[i - 1] == p[i]:
                # a_1 > b_1 or vice versa, so merge the remaining arrays
                k = j - 1
                while k >= 0 and (dp[i - 1][k] == 0 or dp[k][j - 1] == 0):
                    k -= 1
                if k >= 0:
                    dp[i][j] = 1
            else:
                # Both arrays are non-empty and a_1 <= b_1, so we can't merge yet
                dp[i][j] = 0

    return "YES" if dp[2 * n - 1][n] == 1 else "NO"

===END CODE===
