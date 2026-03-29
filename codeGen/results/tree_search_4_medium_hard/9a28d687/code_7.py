import sys

n = int(input())
cost = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = float('inf')
    for j in range(i):
        if strings[j] < strings[i]:
            dp[i] = min(dp[i], dp[j] + cost[i])
        elif strings[j] > strings[i]:
            dp[i] = min(dp[i], dp[j] + 2 * cost[i])

if max(dp) == float('inf'):
    print(-1)
else:
    print(max(dp))
