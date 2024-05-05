def mergeable_permutation():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, n), -1, -1):
            if j == 0:
                dp[i][j] = p[:i] == [x for x in set(p[:i])]
            else:
                for k in range(j):
                    if (p[:k] > p[k:k + j]):
                        break
                for k in range(i - j, i):
                    if (p[k:] < p[i - 1:i]):
                        break
                dp[i][j] = any(dp[x][y] and dp[i - x - 1][j - y] for x in range(k) for y in range(min(j, i - k)))

    return "YES" if dp[n][n] else "NO"
