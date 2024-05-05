from collections import defaultdict

def solve(n, m, T):
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [[0] * (T + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(T + 1):
            if not graph[i]:
                dp[i][j] = dp[i-1][j]
            else:
                max_time_left = T
                visited = 0
                for v, t in graph[i]:
                    if j >= t and dp[v][max_time_left-t] > 0:
                        max_time_left = max(max_time_left - t, 0)
                        visited += 1
                dp[i][j] = visited + (dp[i-1][j] if j == 0 else dp[i-1][min(j, T)])

    return str(dp[n][T]) + "\n" + " ".join(map(str, [i for i in range(1, n+1) if dp[i][T] > 0]))

print(solve(int(input()), int(input()), int(input())))
