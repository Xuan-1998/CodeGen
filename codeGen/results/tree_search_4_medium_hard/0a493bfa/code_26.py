from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[[0] * (m + 1) for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0][0] = 0

    for j in range(n):
        for i in range(min(j, m - 1), -1, -1):
            if a[j] % b[i] == 0:
                good = True
            else:
                good = False

            for prev_good in range(m + 1):
                if good and prev_good > 0:
                    dp[i][j][prev_good] = max(dp[i][j][prev_good], dp[i-1][j-1][prev_good-1] + a[j])
                elif not good and prev_good < m:
                    dp[i][j][prev_good] = max(dp[i][j][prev_good], dp[i-1][j-1][prev_good+1] - a[j])

    return max(max(row) for row in dp[m-1])

print(solve())
