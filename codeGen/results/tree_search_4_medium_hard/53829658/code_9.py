from collections import defaultdict, deque

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)

    reachable = [False] * (n+1)
    reachable[1] = True
    queue = deque([1])
    
    while queue:
        city = queue.popleft()
        for neighbor in graph[city]:
            if not reachable[neighbor]:
                reachable[neighbor] = True
                queue.append(neighbor)

    dp = [float('inf')] * (n+1)
    dp[1] = 0

    min_edges = float('inf')
    capitals = []

    for i in range(2, n+1):
        if not reachable[i]:
            continue
        edges_to_i = len(graph) - graph[i].index(min(graph[i]))
        if edges_to_i < dp[i-1] + 1:
            dp[i] = edges_to_i
            min_edges = min(min_edges, dp[i])
            capitals.append(i)

    print(min_edges)
    print(' '.join(map(str, capitals)))

solve()
