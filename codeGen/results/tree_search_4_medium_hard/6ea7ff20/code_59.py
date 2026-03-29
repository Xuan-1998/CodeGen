from bisect import bisect_left
from collections import defaultdict

n = int(input())
dp = [[False] * (n + 1) for _ in range(n)]

p = list(map(int, input().split()))
for i in range(2 * n):
    if p[i] not in set(p[:i]):
        for j in range(min(i // 2, n), -1, -1):
            if dp[j][i - j]:
                dp[i][j + 1] = True
                break

print('YES' if dp[n][0] else 'NO')
