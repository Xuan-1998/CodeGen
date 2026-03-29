from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for prev in range(i):
            if not graph[prev]:
                dp[i][prev] = 1
            else:
                dp[i][prev] = min(dp[u][v] + 1 for u, edge in enumerate(graph[prev]) if edge[0] == i and edge[1] <= T) or 1

    route = []
    curr = n
    prev = -1
    while curr != 0:
        route.append(curr)
        for neighbor, t in graph[curr]:
            if dp[neighbor][curr] > dp[neighbor][prev]:
                prev = curr
                curr = neighbor
                break
    route.reverse()

    print(len(route))
    print(*route)

if __name__ == "__main__":
    solve()
