from collections import defaultdict

n = int(input())
in_degree = [0] * (n + 1)
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

capital = max(range(1, n + 1), key=lambda x: in_degree[x])
print(in_degree.count(min(in_degree)))
print(*sorted(range(1, n + 1)), key=lambda x: in_degree[x], reverse=True)
