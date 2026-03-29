def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = {}
    ans = "NO"

    for j in range(k+1):
        dp[0] = j == 0

        for (u, v) in edges:
            if v not in dp:
                dp[v] = dp[u][max(0, j-1)]
            else:
                dp[u][max(0, j)] = dp[v][j]

    ans = "YES" if dp[0][k-1] else "NO"

    print(ans)

if __name__ == "__main__":
    solve()
