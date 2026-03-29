import math
from functools import lru_cache

@lru_cache(None)
def digit_length(digit):
    return int(math.ceil(math.log10(digit))) + 1

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = i

for j in range(1, m + 1):
    for i in range(j, n + 1):
        min_length = float('inf')
        for k in range(i - 1, 0, -1):
            min_length = min(min_length, dp[k][j - 1] + digit_length((k % 10) + 1))
        dp[i][j] = min_length

print(dp[n][m])
