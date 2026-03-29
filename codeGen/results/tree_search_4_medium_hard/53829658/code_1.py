from collections import defaultdict

def min_reversed_edges(n, roads):
    # Initialize graph as an adjacency list
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)

    # Perform DFS/BFS from each city to calculate dp[i]
    dp = [float('inf')] * (n + 1)
    visited = set()
    memo = {}

    def dfs(u):
        if u in visited:
            return memo.get(u, float('inf'))
        visited.add(u)
        if dp[u] == float('inf'):
            dp[u] = 0
            for v in graph[u]:
                dp[u] += 1 + dfs(v)
        return dp[u]

    # Calculate dp[i] for each city and update memo
    for i in range(1, n):
        dfs(i)

    # Find the minimum number of edges to be reversed
    min_edges = float('inf')
    capital_cities = []
    for i in range(1, n):
        if dp[i] < min_edges:
            min_edges = dp[i]
            capital_cities = [i]

    for i in range(1, n):
        if dp[i] == min_edges:
            capital_cities.append(i)

    print(min_edges)
    print(' '.join(map(str, capital_cities)))

# Test the code
n = int(input())
roads = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    roads.append((u, v))

min_reversed_edges(n, roads)
