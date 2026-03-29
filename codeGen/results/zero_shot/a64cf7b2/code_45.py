import sys

n, m, T = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    graph[u].append((v, t))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in graph[i]:
        v, t = j
        if dp[v - 1] + t <= T:
            dp[i] = max(dp[i], dp[v - 1] + 1)

path = []
k = dp[n]
i = n

while i > 0 and k > 0:
    for j in graph[i]:
        v, t = j
        if dp[v - 1] + t == dp[i]:
            path.append(i)
            i = v - 1
            k -= 1
            break

print(k)
print(*path[::-1], sep=' ')
