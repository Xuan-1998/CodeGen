from collections import defaultdict

def max_hedgehog_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(m + 1):
            if i > j:
                break
            if j == 0:
                continue
            if i == j:
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
            else:
                dp[i][1] = max(dp[i][1], dp[j - 1][0] + (i - j))
    return dp[n][1]
