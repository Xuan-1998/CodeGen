from collections import deque

def solve():
    n = int(input())
    graph = {}
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    dp = [float('inf')] * (n+1)
    parent = [-1] * (n+1)
    queue = deque([(1, 0)])  # (city, reversed_edges)

    while queue:
        city, reversed_edges = queue.popleft()
        for neighbor in graph.get(city, []):
            if dp[neighbor] > dp[city] + 1:
                dp[neighbor] = dp[city] + 1
                parent[neighbor] = city
                queue.append((neighbor, reversed_edges + 1))

    capital_cities = []
    for i in range(2, n+1):
        if dp[i] == min(dp):
            while i != 1:
                capital_cities.append(i)
                i = parent[i]
            break

    print(min(dp[2:]))
    print(*reversed(capital_cities), sep='\n')

if __name__ == "__main__":
    solve()
