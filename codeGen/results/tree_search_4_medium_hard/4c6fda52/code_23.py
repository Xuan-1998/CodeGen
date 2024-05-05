def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] == 'R' and (i < k or (j % 3 == 0 and i > 0)):
                dp[i][j] = dp[i - 1][j]
            elif s[i - 1] == 'G' and (i < k or (j % 3 == 1 and i > 0)):
                dp[i][j] = dp[i - 1][j]
            elif s[i - 1] == 'B' and (i < k or (j % 3 == 2 and i > 0)):
                dp[i][j] = dp[i - 1][j]
            else:
                if j % 3 == 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                elif j % 3 == 1:
                    dp[i][j] = dp[i - 1][j - 1] + (s[i - 1] != 'R')
                else:
                    dp[i][j] = dp[i - 1][j - 1] + (s[i - 1] != 'G')

    return dp[n][k]

for _ in range(int(input())):
    print(solve())
