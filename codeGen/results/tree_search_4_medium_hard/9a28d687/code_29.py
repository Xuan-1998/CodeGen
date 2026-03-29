import sys
from collections import defaultdict

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * n for _ in range(n)]
prev_chars = defaultdict(list)

for i in range(n):
    prev_chars[costs[i]].append(i)
    dp[i][i] = costs[i]

for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j+1):
            if strings[i+k-1].endswith(strings[k]):
                dp[i][j] = min(dp[i][j], dp[i][k-1] + costs[j] if k > 0 else costs[j])
            else:
                prev_chars[costs[j]].append(j)
                dp[i][j] = min(dp[i][j], dp[i][k-1] + costs[k-1] if k > 0 else costs[0])

print(-1) if dp[0][n-1] == float('inf') else print(dp[0][n-1])
