import sys
from collections import defaultdict, deque

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Create a dictionary to store the in-degree of each node
    in_degree = {i: 0 for i in range(1, n+1)}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize a queue with nodes that have no incoming edges (root nodes)
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    capital_cities = []
    while queue:
        city = queue.popleft()
        capital_cities.append(city)
        for neighbor in graph[city]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Calculate the minimum number of roads to be inverted
    min_inverse_roads = n - len(capital_cities) - 1

    print(min_inverse_roads)
    print(*capital_cities, sep='\n')

if __name__ == "__main__":
    solve()
