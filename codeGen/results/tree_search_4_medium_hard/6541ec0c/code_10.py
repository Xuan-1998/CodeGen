import sys

def xor_tree_values(n, k):
    # Read input from stdin
    _ = int(input())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # DFS to traverse the tree and calculate XOR of values
    memo = {}
    def dfs(node, parent, xor_val):
        if node in memo:
            return memo[node]
        
        visited = set()
        total_xor = 0
        for child in range(n):
            if child == node or edges[child][1] != node:
                continue
            
            # Recursively visit the subtree rooted at the current child
            child_xor, child_visited = dfs(child, node, xor_val ^ values[node])
            
            visited.update(child_visited)
            total_xor ^= child_xor

        memo[node] = (total_xor, visited)
        return memo[node]

    # Calculate XOR of values for each connected component
    connected_components = set()
    for node in range(n):
        if node not in memo:
            xor_val, visited = dfs(node, -1, 0)
            connected_components.add(xor_val)

    # Check if the number of connected components is less than or equal to k
    return 'YES' if len(connected_components) <= k else 'NO'

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(xor_tree_values(n, k))
