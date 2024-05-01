from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k + 1):
            if i == path[j]:
                dp[i][j] = dp[path[j - 1]][j - 1]
            else:
                follow_path = dp[i - 1][j]
                recompute = min(dp[i - 1][k], dp[i][j])
                dp[i][j] = min(follow_path, recompute) + (1 if not follow_path else 0)

    print(min(max(dp[-1]), key=lambda x: x[1]))
