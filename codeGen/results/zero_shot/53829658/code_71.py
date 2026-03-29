import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for i in range(1, n):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        in_degree[v] += 1

    # Initialize queue with nodes having no incoming edges
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    
    capital_cities = []
    reversed_edges = 0
    
    while queue:
        city = queue.popleft()
        capital_cities.append(city)
        
        for neighbor in graph[city]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Calculate the minimum number of reversed edges needed to reach any other city from the capital
    for i in range(n):
        if i not in capital_cities:
            while graph[i]:
                neighbor = graph[i].pop()
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    break
            reversed_edges += len(graph[i])
    
    print(reversed_edges)
    print(' '.join(map(str, capital_cities)))

if __name__ == "__main__":
    main()
