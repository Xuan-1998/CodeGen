from collections import deque, defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)
s, t = 0, n-1
path = list(map(int, input().split()))
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def bfs(s, t, path):
    q = deque([(s, 0)])
    dp = [float('inf')] * n
    parent = [-1] * n
    dp[s] = 0
    while q:
        v, d = q.popleft()
        for w in graph[v]:
            if w == t:
                return d + 1
            if dp[w] > d + 1:
                dp[w] = d + 1
                parent[w] = v
                q.append((w, d + 1))
    return -1

min_val = bfs(s, t, path)
max_val = bfs(t, s, list(reversed(path)))
print(min_val, max_val)
