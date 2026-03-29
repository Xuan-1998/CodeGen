import sys

n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(m):
    queries.append(tuple(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
for i in range(1, n+1):
    for j in range(n):
        dp[i][j] = max(dp[i-1].index(k) if k <= array[j] else -1 for k in range(n)) + 1

for l, r in queries:
    if any(dp[i][r] > dp[i-1][r] or dp[i][r] > r for i in range(1, n+1)):
        print("No")
    else:
        print("Yes")
