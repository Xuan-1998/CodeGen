from collections import defaultdict

def hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if not any(k in [u for u in graph[i]] or k in [v for v in graph[j]] for k in range(j)):
                dp[i][j] = (j - i) * len([k for k in range(i, j)])
    return max(max(row) for row in dp)

print(hedgehog_beauty())
