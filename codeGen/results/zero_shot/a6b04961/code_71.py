def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

def find_longest_tail(n, m, edges):
    # Use DFS or BFS to find the longest simple path (tail)
    tail_length = 0
    visited = [False] * (n + 1)
    current_path = []
    for edge in edges:
        u, v = edge
        if not visited[u]:
            dfs(u, n, m, edges, visited, current_path, &lt;tail_length&gt;)
    return tail_length

def count_spines(n, m, edges, tail_length):
    # Count the number of spines by iterating through all edges
    spine_count = 0
    for edge in edges:
        u, v = edge
        if not (u &lt;= tail_length and v &lt;= tail_length):
            spine_count += 1
    return spine_count

def main():
    n, m, edges = read_input()
    tail_length = find_longest_tail(n, m, edges)
    spine_count = count_spines(n, m, edges, tail_length)
    print(tail_length * spine_count)

if __name__ == "__main__":
    main()
