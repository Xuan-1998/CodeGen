import sys
from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(i, time_left):
        if visited[i]:
            return 0
        visited[i] = True
        max_visit = 1
        for j, t in graph[i]:
            if time_left >= t:
                visit = dfs(j, time_left - t) + 1
                max_visit = max(max_visit, visit)
        return max_visit

    dp[n] = 1
    for i in range(n - 1, -1, -1):
        visited[i] = False
        if i != n:
            dp[i] = dfs(i, T)

    max_visit = 0
    route = []
    for i in range(1, n + 1):
        if dp[i] > max_visit:
            max_visit = dp[i]
            route = [i]
        elif dp[i] == max_visit:
            route.append(i)

    print(max_visit)
    print(' '.join(map(str, route)))

if __name__ == "__main__":
    solve()
