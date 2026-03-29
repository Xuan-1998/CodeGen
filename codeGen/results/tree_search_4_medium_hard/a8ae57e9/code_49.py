code
from collections import defaultdict

def solve(n, k, m, requests):
    dp = [[0] * (m + 1) for _ in range(k + 1)]

    for size, money in requests:
        for i in range(k, size - 1, -1):
            if money <= i:
                dp[i][money] = max(dp[i][money], dp[i - size][money - size] + money)
        for j in range(m, money - 1, -1):
            if j >= money:
                dp[k][j] = max(dp[k][j], dp[k][j - money] + money)

    return dp[k][m]

n, k, m = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(n)]
print(*solve(n, k, m, requests), sep='\n')
