import sys
from collections import defaultdict, deque

def count_pairs(n, k, edges):
    # Create adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Function to perform BFS and return distances from the start node
    def bfs(start):
        distances = [-1] * (n + 1)
        distances[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        return distances

    # Count pairs with exactly k distance
    pair_count = 0
    for i in range(1, n + 1):
        distances = bfs(i)
        distance_count = [0] * (k + 1)
        for dist in distances:
            if dist <= k:
                distance_count[dist] += 1
        if k < len(distance_count):
            pair_count += distance_count[k]
    
    # Each pair is counted twice, so divide by 2
    return pair_count // 2

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    result = count_pairs(n, k, edges)
    print(result)

