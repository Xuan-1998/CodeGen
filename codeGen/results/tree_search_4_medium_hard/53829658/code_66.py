import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    # Find the capital city with maximum in-degree
    max_in_degree = 0
    capital = None
    for city in range(1, n+1):
        in_degree = len(graph[city])
        if in_degree > max_in_degree:
            max_in_degree = in_degree
            capital = city

    # Calculate the minimum number of reversed roads needed to reach each city from the capital
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        if i != capital:
            for j in range(i+1, n+1):
                if graph[i]:
                    min_reversed_roads = float('inf')
                    for neighbor in graph[i]:
                        if neighbor < j:
                            min_reversed_roads = min(min_reversed_roads, dp[neighbor][j] + 1)
                    dp[i][j] = min_reversed_roads

    # Find all possible ways to choose the capital
    parent = [None] * (n+1)
    for i in range(1, n+1):
        if i != capital:
            prev_city = None
            for neighbor in graph[i]:
                if dp[neighbor][i] + 1 < dp[i][i]:
                    prev_city = neighbor
                    parent[i] = neighbor
                    break

    # Print the minimum number of reversed roads and all possible ways to choose the capital
    min_reversed_roads = dp[max_in_degree]
    print(min_reversed_roads)
    if parent:
        capital_cities = [capital]
        while parent[capital]:
            capital = parent[capital]
            capital_cities.append(capital)
        print(' '.join(map(str, reversed(capital_cities))))

if __name__ == "__main__":
    solve()
