from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
p = list(map(int, input().split()))

dp = [0] * (max(n, k))
for j in range(1, k + 1):
    if p[j - 1] == p[j - 2]:
        dp[j] = dp[j - 1]
    else:
        dp[j] = 1

min_recomputations = sum(1 for i in range(k) if p[i] != p[i - 1])
max_recomputations = k - 2

print(min_recomputations, max_recomputations)
