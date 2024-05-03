from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    plants = [list(map(int, input().split())) for _ in range(n)]

    # Create a graph where each node is a species and an edge represents the possibility of replanting
    graph = defaultdict(list)
    for i in range(n):
        s, x = plants[i]
        if i > 0:
            prev_s, prev_x = plants[i-1]
            if prev_s != s:
                graph[prev_s].append(s)
        if i < n - 1:
            next_s, next_x = plants[i+1]
            if next_s != s:
                graph[s].append(next_s)

    # Perform BFS to find the minimum number of replantings
    visited = set()
    min_replantings = float('inf')
    for species in range(1, m + 1):
        queue = deque([(species, 0)])
        while queue:
            node, depth = queue.popleft()
            if node not in visited:
                visited.add(node)
                if len(graph[node]) > 0:
                    min_replantings = min(min_replantings, depth + 1)
                    for neighbor in graph[node]:
                        queue.append((neighbor, depth + 1))

    print(min_replantings)

if __name__ == "__main__":
    solve()
