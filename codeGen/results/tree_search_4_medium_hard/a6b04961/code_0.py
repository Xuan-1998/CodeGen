import sys

n, m = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    dp[max(u, v)] += 1
max_beauty = max((dp[j] * (i - j) for i in range(2, n + 1) for j in range(1, i)))
print(max_beauty)
