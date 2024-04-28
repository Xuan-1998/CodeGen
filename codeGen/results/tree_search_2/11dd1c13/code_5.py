import sys
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n)]
for i in range(n):
    for k in range(1, n + 1):
        min_sum = sys.maxsize
        for j in range(n):
            if i > 0 and dp[i - 1][j] != 0:
                new_sum = dp[i - 1][j] - grid[i][j]
                if new_sum < min_sum:
                    min_sum = new_sum
        dp[i][k] = min_sum

print(min(dp[-1]))
