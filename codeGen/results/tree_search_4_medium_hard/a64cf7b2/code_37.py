import sys

n, m, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    for t in range(T, -1, -1):
        dp[i][t] = max(dp[i][t], dp[i + 1][min(t, T)] + 1)

k = dp[1][T]
print(k)

for i in range(k):
    print((dp.index([x for x in dp if x == [max(dp[:i+1]), k-i-1]]))[0] + 1)
