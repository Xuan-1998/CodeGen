from collections import defaultdict

def min_max_recomputations(n, m, edges, k, p):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    f = [0] * (n + 1)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, p[k - 1] + 1):
            if has_edge(j, i):
                f[i] = min(f[j] + 1, f[i])
        dp[p[k - 1]] = max(dp[p[k - 1]], f[p[k - 1]])

    return dp[0], dp[-1]

def has_edge(u, v):
    # Check if there's an edge from u to v
    pass

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    p = list(map(int, input().split()))

    dp_min, dp_max = min_max_recomputations(n, m, edges, k, p)

    print(dp_min, dp_max)
