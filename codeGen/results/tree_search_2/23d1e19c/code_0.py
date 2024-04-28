def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        if i == s:
            dp[i][0] = dp[i][1] = float('inf')
        elif i == t:
            dp[i][0] = dp[i][1] = 0
        else:
            if graph[i]:
                j = path.index(i)
                if j > 0:
                    prev_path_len = len(path[:j])
                    dp[i][0] = min(dp[path[j-1]][0], dp[i][0]) + (dp[path[j-1]][0] - dp[path[j-2]][0] + 1) if j > 1 else dp[i][0]
                    dp[i][1] = max(dp[path[j-1]][1], dp[i][1]) + (dp[path[j-1]][1] - dp[path[j-2]][1] + 1) if j > 1 else dp[i][1]

    print(*[str(min(dp[i])) for i in range(1, n+1)], sep=' ')
    print(*[str(max(dp[i])) for i in range(1, n+1)], sep=' ')

if __name__ == '__main__':
    solve()
