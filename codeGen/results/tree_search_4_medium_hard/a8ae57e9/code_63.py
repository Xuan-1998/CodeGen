code
from collections import namedtuple

Request = namedtuple('Request', ['group_size', 'amount'])

n, k = map(int, input().split())
requests = [Request(*map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i <= j and requests[i - 1].group_size <= j:
            dp[i][j] = max(dp[i - 1][j], requests[i - 1].amount)
        else:
            dp[i][j] = dp[i - 1][j]
        for table in range(1, min(i, j) + 1):
            dp[i][j] = max(dp[i][j], dp[table - 1][j - table] + requests[i - 1].amount)

print(f"{dp[n][k]}")
for i in range(n, 0, -1):
    if dp[i][k] != dp[i - 1][k]:
        print(f"{i} {requests[i - 1].group_size} {k - (i - requests[i - 1].group_size)}")
        k -= requests[i - 1].group_size
