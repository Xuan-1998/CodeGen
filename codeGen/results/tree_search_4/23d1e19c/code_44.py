from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == s:
            continue
        for j in range(k + 1):
            min_recomputation = float('inf')
            for v in graph[i]:
                if v not in path[:j]:
                    min_recomputation = min(min_recomputation, dp[path.index(v)][j - 1] + 1)
            dp[i][j] = min_recomputation

    return f"{dp[t][k]} {dp[t][k]}"

print(solve())
