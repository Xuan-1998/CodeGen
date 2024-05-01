import sys

n, m = map(int, input().split())
dp = [[0, 0] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    # ... (insert edge processing code here)

k = int(input())
path = list(map(int, input().split()))

for i in range(1, k + 1):
    if path[i - 1] != path[i]:
        dp[path[i - 1]][0] += 1
        dp[path[i - 1]][1] += 1

min_recomps = sys.maxsize
max_recomps = 0

for i in range(n):
    min_recomps = min(min_recomps, dp[i][0])
    max_recomps = max(max_recomps, dp[i][1])

print(f"{min_recomps} {max_recomps}")
