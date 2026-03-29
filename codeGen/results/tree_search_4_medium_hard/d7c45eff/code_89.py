def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j < k:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + (s[i - 1] != s[j - 1]))
            else:
                dp[i][j] = dp[i - 1][j]

    result = []
    for i in range(n, -1, -1):
        if k > 0 and dp[i][k]:
            k -= 1
        else:
            result.append(s[i])

    return ''.join(reversed(result))
