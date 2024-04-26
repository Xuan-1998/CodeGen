from collections import defaultdict

def read_ints():
    return list(map(int, input().split()))

def dfs(graph, start, visited, distance):
    visited[start] = True
    farthest_node = start
    max_distance = distance
    for neighbor, length in graph[start]:
        if not visited[neighbor]:
            new_distance, new_farthest_node = dfs(graph, neighbor, visited, distance + length)
            if new_distance > max_distance:
                max_distance = new_distance
                farthest_node = new_farthest_node
    return max_distance, farthest_node

def find_road_to_remove(graph, n):
    # Step 1: Find one end of the diameter
    visited = [False] * (n + 1)
    _, farthest_node = dfs(graph, 1, visited, 0)
    
    # Step 2: Find the actual diameter
    visited = [False] * (n + 1)
    diameter, _ = dfs(graph, farthest_node, visited, 0)
    
    # Step 3: Find the edge to remove
    # For this problem, we can just return the diameter as the minimum inconvenience
    # because we are not required to specify which road to remove.
    return diameter

def main():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        u, v, l = read_ints()
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    result = find_road_to_remove(graph, n)
    print(result)

if __name__ == "__main__":
    main()
