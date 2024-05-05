import sys

def find_longest_path(graph):
    # Implement dynamic programming or Bellman-Ford algorithm to find the longest path
    pass

def count_spines(longest_path, graph):
    # Count the number of spines by iterating over edges and checking if they have one endpoint in the longest path
    pass

def calculate_beauty(longest_path_length, spine_count):
    return longest_path_length * spine_count

n, m = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = graph.get(u, []) + [v]
    graph[v] = graph.get(v, []) + [u]

longest_path_length = find_longest_path(graph)
spine_count = count_spines(longest_path_length, graph)
beauty = calculate_beauty(longest_path_length, spine_count)

print(beauty)
