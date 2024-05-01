import sys

n, m = map(int, input().split())
dp = [0] * (n + 1)
max_rec = 0

for _ in range(m):
    u, v = map(int, input().split())
    dp[v] = max(dp[v], dp[u] + 1)

k = int(input())
path = list(map(int, input().split()))
path_set = set(path[1:])

min_rec = sys.maxsize
for i in range(k):
    if path[i] not in path_set:
        min_rec = min(min_rec, dp[path[i-1]] + 1)

print(f"{min_rec} {max_rec}")
