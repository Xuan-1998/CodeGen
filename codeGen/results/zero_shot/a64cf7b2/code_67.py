import sys
from collections import defaultdict, deque

def dfs(graph, time_limit):
    n = len(graph)
    visited = [False] * (n + 1)
    dp = [[0, []] for _ in range(n + 1)]
    queue = deque([(1, 0)])

    while queue:
        node, current_time = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for neighbor, edge_time in graph[node].items():
                next_time = current_time + edge_time
                if next_time <= time_limit and dp[neighbor][0] < next_time:
                    dp[neighbor] = [next_time, dp[node][1] + [node]]
                    queue.append((neighbor, next_time))
    return max(dp[n], key=lambda x: (x[0], -len(x[1])))

def main():
    n, m, T = map(int, sys.stdin.readline().split())
    graph = defaultdict(dict)
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u][v] = t

    max_vertices = dfs(graph, T)
    print(max_vertices[0])
    print(' '.join(map(str, max_vertices[1])))

if __name__ == "__main__":
    main()
