===BEGIN CODE===
from collections import deque

def shortest_path_recomputation():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}
    fixed_path = list(map(int, input().split()))
    s, t = fixed_path[0], fixed_path[-1]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    min_dp = [[float('inf')] * (n+1) for _ in range(n+1)]

    queue = deque([(s, 0)])
    while queue:
        node, count = queue.popleft()
        if node == t:
            break
        for neighbor in graph[node]:
            if neighbor not in fixed_path:
                dp[neighbor][count+1] = min(dp[neighbor][count+1], dp[node][count]+1)
                min_dp[neighbor][count+1] = min(min_dp[neighbor][count+1], min_dp[node][count]+1)
                queue.append((neighbor, count+1))

    print(min(dp[t][-1]), max(dp[t][-1]))

shortest_path_recomputation()
