import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    prev_v, prev_path = None, []

    dp = [[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        if graph[i]:
            min_rec, max_rec = sys.maxsize, 0
            for j in range(len(graph[i])):
                v = graph[i][j]
                if (v, prev_path + [i]) == (path[k-1], path[:k-1]):
                    min_rec = min(min_rec, dp[prev_v][len(prev_path)])
                    max_rec = max(max_rec, dp[prev_v][len(prev_path)])
            dp[i] = [min_rec+1, max_rec+1]
        else:
            dp[i] = [0, 0]

    print(*dp[t])

solve()
