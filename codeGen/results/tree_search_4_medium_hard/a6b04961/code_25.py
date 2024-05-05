def hedgehog_beauty(n, m, edges):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for k in range(i):
            if k > 0:
                dp[i][k] = max(dp[i][k], dp[i - 1][k - 1] + (i - 1) * k)
            else:
                dp[i][k] = dp[i - 1][k]

    for i in range(2, n + 1):
        for edge in edges:
            if edge[0] < i and edge[1] < i:
                u, v = sorted(edge)
                for k in range(i):
                    dp[u][k] = max(dp[u][k], dp[v][k - 1] + (i - 1) * k)

    return dp[-1][-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(hedgehog_beauty(n, m, edges))
