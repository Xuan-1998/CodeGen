import heapq

def solve(n, edges, m, k):
    # Create a graph from the given edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize memoization table
    dp = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(n)]

    # Function to check if there exists an edge between two nodes with label sum equal to k
    def has_edge(u, v, k):
        if k < 0:
            return False
        if dp[u][v][k]:
            return True
        for w in graph[u]:
            if w == v:
                continue
            if has_edge(w, v, k - u + v):
                dp[u][v][k] = True
                return True
        return False

    # Calculate the maximum possible distribution index of the tree
    max_dist_index = 0
    for i in range(n):
        for j in range(i + 1, n):
            if has_edge(i, j, k):
                dist_index = sum(range(i + 1, j)) % (10**9 + 7)
                max_dist_index = max(max_dist_index, dist_index)

    return max_dist_index

# Read input from stdin
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
m = int(input())
k = list(map(int, input().split()))

# Calculate and print the result
print(solve(n, edges, m, k) % (10**9 + 7))
