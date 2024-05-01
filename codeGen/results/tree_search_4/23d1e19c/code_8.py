def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for u, v in (map(int, input().split()) for _ in range(m)):
        graph[u-1].append(v)
    k = int(input())
    p = list(map(int, input().split()))
    memo = {k: k for k in range(n+1)}

    def f(k):
        return memo.get(k, k) if k < n else 0

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][j] = j for j in range(k+1)]

    for i in range(1, n+1):
        for j in range(min(i, k), -1, -1):
            if p[j-1] == i:
                dp[i][j] = min(dp[i][j-1], 1 + f(j-2))
            else:
                dp[i][j] = dp[i-1][j]

    return min(max(dp[i][k] for i in range(1, n+1)), k)
