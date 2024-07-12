import sys
from collections import defaultdict, deque

input = sys.stdin.read

def count_pairs_with_distance_k(n, k, edges):
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # To store the result
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        # Distance array to count nodes at each distance from the current node
        distance_count = [0] * (k + 1)
        distance_count[0] = 1  # The node itself is at distance 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_count = dfs(neighbor, node)
            
            # Combine results from children
            for i in range(k):
                result += distance_count[i] * child_count[k - i - 1]
            
            # Update distance_count with child_count
            for i in range(k):
                distance_count[i + 1] += child_count[i]
        
        return distance_count
    
    # Start DFS from node 1 (assuming 1-based indexing)
    dfs(1, -1)
    
    return result

def main():
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
    
    result = count_pairs_with_distance_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

