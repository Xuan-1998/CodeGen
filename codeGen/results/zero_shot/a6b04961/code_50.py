import sys

def dfs(graph, visited, vertex):
    if visited[vertex]:
        return 0
    visited[vertex] = True
    max_path_length = 1
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            max_path_length += dfs(graph, visited, neighbor)
    return max_path_length

def find_longest_path_and_spines(graph):
    n = len(graph)
    visited = [False] * n
    longest_path_length = 0
    for vertex in range(n):
        if not visited[vertex]:
            path_length = dfs(graph, visited, vertex)
            longest_path_length = max(longest_path_length, path_length)

    spines = 0
    for edge in graph:
        u, v = edge
        if u != v and (u not in visited or v not in visited):
            spines += 1

    return longest_path_length * spines

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph.append((u - 1, v - 1))  # subtract 1 since indices start at 0

    max_beauty = find_longest_path_and_spines(graph)
    print(max_beauty)

if __name__ == "__main__":
    main()
