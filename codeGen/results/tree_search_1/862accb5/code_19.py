import sys
from collections import defaultdict, deque

def dfs(graph, start, parent, visited, stack):
    visited[start] = True
    stack.append(start)

    for neighbor, length in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, start, visited, stack):
                return True
        elif neighbor != parent:
            # Found a cycle
            return True

    stack.pop()
    return False

def find_cycle(graph, n):
    visited = [False] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(graph, i, -1, visited, stack):
                return stack
    return None

def calculate_inconvenience(graph, cycle, n):
    def bfs(start, excluded):
        queue = deque([(start, 0)])
        visited = [False] * (n + 1)
        visited[start] = True
        total_distance = 0

        while queue:
            node, distance = queue.popleft()
            total_distance += distance

            for neighbor, length in graph[node]:
                if not visited[neighbor] and (node, neighbor) not in excluded and (neighbor, node) not in excluded:
                    visited[neighbor] = True
                    queue.append((neighbor, distance + length))

        return total_distance

    min_inconvenience = float('inf')
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        inconvenience = bfs(u, {(u, v), (v, u)}) + bfs(v, {(u, v), (v, u)}) + graph[u][v]
        min_inconvenience = min(min_inconvenience, inconvenience)

    return min_inconvenience

def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(list)

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    cycle = find_cycle(graph, n)
    result = calculate_inconvenience(graph, cycle, n)
    print(result)

if __name__ == "__main__":
    main()
